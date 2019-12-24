import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

def get_numbers(text):
    return re.sub(r'[^0-9.]', '', text)


def basic_clean(text):
    """
    Lowercase everything
    Normalize unicode characters
    Replace anything that is not a letter, number, whitespace or a single quote
    """
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r"[^a-z0-9'\s]", '', text)
    text = re.sub(r"[\r|\n|\r\n]+", ' ', text)
    return text

def different_clean(text):
    """
    Lowercase everything
    Normalize unicode characters
    Replace anything that is not a letter with a space
    Remove any words that are 2 or less characters   
    Strip all white spaces that are more than one
    Strip the beginning and end of whitespace 
    """
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r"[^a-z]", ' ', text)
    text = re.sub(r'\b[a-z]{,2}\b', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def remove_things(text):    
    text = re.sub(r"[^a-z0-9]", ' ', text)
    text = re.sub(r'\b[a-z]{,2}\b', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def remove_stopwords(text):
    """
    accept some text and return the text after removing all the stopwords.
    """
    stopword_list = stopwords.words('english')
    words = text.split()
    filtered_words = [w for w in words if w not in stopword_list]
    return ' '.join(filtered_words)


def tokenize(text):
    """
    take in a string and tokenize all the words in the string.
    """
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(text, return_str=True)

def lemmatize(text):
    """
    accept some text and return the text after applying lemmatization to each word.
    """
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    return ' '.join(lemmas)

def stem(text):
    """
    accept some text and return the text after applying stemming to all the words.
    """
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed