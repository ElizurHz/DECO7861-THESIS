import sys
sys.path.append("..")
import numpy as np
import itertools
from sklearn.feature_extraction.text import *
from text.text_preprocessing import *
from gensim import models
from gensim import corpora
from sklearn.cluster import *
from sklearn import metrics
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from pymongo import *

def tf_idf(texts):
    wordset = ""
    textset = []
    # join the words
    for text in texts:
        for word in text:
            wordset = wordset + word + " "
        textset.append(wordset)
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tf_idf = transformer.fit_transform(vectorizer.fit_transform(textset))
    words = vectorizer.get_feature_names()
    weight = tf_idf.toarray()
    '''
    for i in range(len(weight)):
        print("---------THE TF-IDF WEIGHT OF NO.", i, " TEXT-----------")
        for j in range(len(words)):
            print(words[j], weight[i][j])
    '''
    return weight, words


def get_descriptions(weight, words, num, username):
    print("---------THE TF-IDF WEIGHT FOR ", username[num], "-----------")
    for i in range(len(words)):
        print(words[i], weight[num][i])

'''
def tfidf_gensim(dictionary, texts):
    tf = [dictionary.doc2bow(text) for text in texts]
    tfidf_model = models.TfidfModel(tf)
    tfidf = tfidf_model[tf]
    return tfidf


def lda_analysis_single(dir, user):
    texts = preprocessing_single_user(dir, user)
    dictionary = corpora.Dictionary(texts)
    tfidf = tfidf_gensim(dictionary, texts)
    lda = models.ldamodel.LdaModel(tfidf, id2word=dictionary, num_topics=3)
    print(lda.print_topics(num_topics=3, num_words=5))


def lda_analysis_multiple(dir, users):
    texts = preprocessing_multiple_users(dir, users)
    dictionary = corpora.Dictionary(texts)
    tfidf = tfidf_gensim(dictionary, texts)
    lda = models.ldamodel.LdaModel(tfidf, id2word=dictionary, num_topics=3)
    print(lda.print_topics(num_topics=3, num_words=5))


def clustering_lda_analysis_single(dir, user, nodes):
    texts = preprocessing_single_user(dir, user)
    clustering_texts = []
    for node_num in nodes:
        text = texts[node_num]
        clustering_texts.append(text)
    dictionary = corpora.Dictionary(clustering_texts)
    tfidf = tfidf_gensim(dictionary, clustering_texts)
    lda = models.ldamodel.LdaModel(tfidf, id2word=dictionary, num_topics=3)
    print(lda.print_topics(num_topics=3, num_words=5))


def clustering_lda_analysis_multiple(dir, users, nodes):
    texts = preprocessing_multiple_users(dir, users)
    clustering_texts = []
    for node_num in nodes:
        text = texts[node_num]
        clustering_texts.append(text)
    dictionary = corpora.Dictionary(clustering_texts)
    tfidf = tfidf_gensim(dictionary, clustering_texts)
    lda = models.ldamodel.LdaModel(tfidf, id2word=dictionary, num_topics=3)
    print(lda.print_topics(num_topics=3, num_words=5))


def agg_clu_single(dir, user):
    # Create Agglomerative Clustering model
    texts = preprocessing_single_user(dir, user)
    vectors, words = tf_idf(texts)
    ac = AgglomerativeClustering()
    model = ac.fit(vectors)
    labels = model.labels_

    # Plotting dendrogram
    children = model.children_
    distance = np.arange(children.shape[0])
    no_of_observations = np.arange(2, children.shape[0] + 2)
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)
    dendrogram(linkage_matrix)
    plt.show()

    # Construct the dendrogram tree
    ii = itertools.count(vectors.shape[0])
    tree = [{'node_id': next(ii), 'left': x[0], 'right': x[1]} for x in model.children_]
    print(tree)

    # get node ids for each cluster
    root_list = [194, 195, 192, 193]     # value can be changed after plotting original dendrogram
    nodes = []
    for root in root_list:
        node_list = []
        node_list.append(get_all_leaves(len(vectors), root, tree, node_list))
        del node_list[-1]
        nodes.append(node_list)
    return nodes, labels
'''

def get_all_leaves(count, root, tree, node_list):
    if root < count:
        node_list.append(root)
        return root
    else:
        for node in tree:
            if node['node_id'] == root:
                current_node = node
        get_all_leaves(count, current_node['left'], tree, node_list)
        get_all_leaves(count, current_node['right'], tree, node_list)


def agg_clu_multiple(dir, users):
    # Create Agglomerative Clustering model
    texts, username = preprocessing_multiple_users(dir, users)
    vectors, words = tf_idf(texts)
    ac = AgglomerativeClustering()
    model = ac.fit(vectors)
    labels = model.labels_

    # Plotting dendrogram
    children = model.children_
    distance = np.arange(children.shape[0])
    no_of_observations = np.arange(2, children.shape[0] + 2)
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)
    dendrogram(linkage_matrix)
    plt.show()

    # Construct the dendrogram tree
    ii = itertools.count(vectors.shape[0])
    tree = [{'node_id': next(ii), 'left': x[0], 'right': x[1]} for x in model.children_]
    print(tree)

    # get node ids for each cluster
    root_list = [160, 163, 164]  # value can be changed after plotting original dendrogram
    nodes = []
    for root in root_list:
        node_list = []
        node_list.append(get_all_leaves(len(vectors), root, tree, node_list))
        del node_list[-1]
        nodes.append(node_list)
    return nodes, labels


def silhouette_score(vectors, labels):
    return metrics.silhouette_score(vectors, labels, metric='euclidean')


if __name__ == '__main__':
    '''
    texts = preprocessing_single_user('hs', 'firebat')
    vectors = tf_idf(texts)

    # Single user
    lda_analysis_single('hs', 'firebat')
    nodes_list, labels = agg_clu_single('hs', 'firebat')
    for nodes in nodes_list:
        clustering_lda_analysis_single('hs', 'firebat', nodes)
    print("The Silhouette score is: " + str(silhouette_score(vectors, labels)))
    '''
    # Multiple users
    client = MongoClient()
    db = client['twitter']
    col = db['list_members_h_s']

    texts, username = preprocessing_multiple_users('hs', col.find())
    vectors, words = tf_idf(texts)

    nodes_list, labels = agg_clu_multiple('hs', col.find())
    print(nodes_list)

    get_descriptions(vectors, words, 69, username)

    print("The Silhouette score is: " + str(silhouette_score(vectors, labels)))
