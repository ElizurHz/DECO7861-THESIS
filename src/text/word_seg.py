import nltk
import os
import math
import string
import jieba.posseg as pseg
from sklearn.feature_extraction.text import TfidfVectorizer

def read_file_as_str(user):
    if not os.path.isfile("user_timeline_" + user + ".txt"):
        raise TypeError("user_timeline_" + user + ".txt" + " does not exist")
    all_the_text = open("user_timeline_" + user + ".txt").read()
    return all_the_text

def get_tokens(text):
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
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