import os
import string
import nltk
import jieba.posseg as pseg
from nltk.corpus import stopwords
from nltk.stem.porter import *
from konlpy.corpus import kobill


def get_tokens(text):
    lowers = text.lower()
    # Remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def chn_seg(text):
    words = pseg.cut(text)
    return words


def eng_preprocessing_single_user(user):
    # read a set of tweets from a single user

    # input: username
    # output: a list with tweets after stemming
    tweets = []
    for line in open('output/' + user + "_user_timeline.txt"):
        line_filtered = re.sub('"', '', line)
        tweets.append(line_filtered)
    f = open('output/' + user + "_stemmed.txt", "w")
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
    return tweets_stemmed


def eng_preprocessing_multiple_users(users):
    # read all tweets as a string and integrate them

    # input: a list of users
    # output: a dictionary, keys: users, values: tweets after stemming
    documents = {}
    documents_stemmed = {}
    for user in users:
        document = read_file_as_str(user)
        documents[user] = document
    for user in documents.keys():
        output = ""
        tokens = get_tokens(documents[user])
        filtered = [w for w in tokens if not w in stopwords.words('english')]
        stemmer = PorterStemmer()
        stemmed = stem_tokens(filtered, stemmer)
        for stem in stemmed:
            output = output + stem + " "
        documents_stemmed[user] = output
    return documents_stemmed


def read_file_as_str(user):
    if not os.path.isfile('output/' + user + "user_timeline.txt"):
        raise TypeError('output/' + user + "user_timeline.txt" + " does not exist!")
    all_the_text = open('output/' + user + "user_timeline.txt").read()
    return all_the_text
