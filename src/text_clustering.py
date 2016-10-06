from word_seg import *
import re
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
from sklearn.feature_extraction.text import *

if __name__ == '__main__':
    # word segmentation
    # account for testing
    user = "LFC"
    tweets = []
    for line in open("user_timeline_" + user + ".txt"):
        line_filtered = re.sub('"', '', line)
        tweets.append(line_filtered)
    f = open(user + "_stemmed.txt", "w")
    tweets_stemmed = []
    for tweet in tweets:
        output = ""
        tokens = get_tokens(tweet)
        filtered = [w for w in tokens if not w in stopwords.words('english')]
        stemmer = PorterStemmer()
        stemmed = stem_tokens(filtered, stemmer)
        for stem in stemmed:
            output = output + stem + " "
        f.write(output + " \n")
        tweets_stemmed.append(output)
    f.close()
    # TF-IDF
    corpus = ["我 来到 北京 清华大学",
              "他 来到 了 网易 杭研 大厦",
              "小明 硕士 毕业 与 中国 科学院",
              "我 爱 北京 天安门"]
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(tweets_stemmed))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    for i in range(len(weight)):
        print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])
    '''

    f = open(user + "_stemmed.txt", "w")
    for stem in stemmed:
        f.write(stem + ' ')
    f.close()
    # count = Counter(stemmed)
    # print(count.most_common(20))
    '''

    # clustering
    # VSM 矩阵计算相似度来进行聚类


    # Result (output & plot)
