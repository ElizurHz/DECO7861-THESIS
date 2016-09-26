from word_seg import *
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *

if __name__ == '__main__':
    # word segmentation
    # account for testing
    user = "LFC"
    tweet = read_file_as_str(user)
    tokens = get_tokens(tweet)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()
    stemmed = stem_tokens(filtered, stemmer)
    count = Counter(stemmed)
    print(count.most_common(20))
    # TF-IDF

    # clustering
    # TF-IDF 矩阵计算相似度来进行聚类


    # Result (output & plot)
