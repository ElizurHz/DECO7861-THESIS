from pymongo import *
from sklearn.feature_extraction.text import *


def tf_idf(tweets):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tf_idf = transformer.fit_transform(vectorizer.fit_transform(tweets))
    word = vectorizer.get_feature_names()
    weight = tf_idf.toarray()
    for i in range(len(weight)):
        print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
        for j in range(len(word)):
            print(word[j], weight[i][j])
    return weight
