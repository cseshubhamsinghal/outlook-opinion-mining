import datetime


import pandas as pd
import numpy as np
import re

import pickle

#--------------------------------------------------------------------------------------------------------------------------------------------
## import the file responsible for Doc2Vec feature extraction of the tweets

import gensim.models as g
import codecs

#--------------------------------------------------------------------------------------------------------------------------------------------
## import the nltk packages

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

#--------------------------------------------------------------------------------------------------------------------------------------------
## preprocessing of each row of csv file

def preprocess(tweet):
    stop_words = set(stopwords.words('english'))                            ## stopwords removal
    
    word_tokens = word_tokenize(tweet)                                      ## tokenization

    lemmatizer = WordNetLemmatizer()                                        ## lemmatization

    ps = PorterStemmer()                                                    ## stemming

    allowed_word_types = ['WP','JJ','JJR','JJS','NN','CD']                  ## part of speech tagging
    
    filtered = []

    for w in word_tokens:
        if w not in stop_words:
            filtered.append(lemmatizer.lemmatize(w,pos="a"))
            
    filtered_sentence = []

    for p in filtered:
        pos = nltk.pos_tag(p)
        if pos[0][1] in allowed_word_types:
            filtered_sentence.append(p)


## FEATURE ENGINEERING
    ##----------------------------------------------------------------------
    ## count of negative words in a row
    
    fo = open("dictionary/negative-words.txt", "r")

    for row in fo:
        line = fo.read()
    word_tokens = word_tokenize(line)

    count = 0

    for words in filtered_sentence:
        if words in word_tokens:
            count+=1
            
    li=[]
    
    li.append(count)

    ##----------------------------------------------------------------------
    ## count of positive words in a row
    
    f1 = open("dictionary/positive-words.txt", "r")

    for row in f1:
        line1 = f1.read()
    word_tokens1 = word_tokenize(line1)

    count1 = 0

    for words in filtered_sentence:
        if words in word_tokens1:
            count1+=1

    li.append(count1)

    

#--------------------------------------------------------------------------------------------------------------------------------------------
    # Open a file
    fo = open("tweet.txt", "w")
    fo.write(tweet)

    # Close opend file
    fo.close()


# infer document vectors from model trained for performing doc2vec 

#parameters

    model="doc2vec-master/toy_data/model.bin"
    test_docs="tweet.txt"
    output_file="tweet_vectors.txt"

    start_alpha=0.01            # the initial learning rate.
    infer_epoch=1000

#load model

    m = g.Doc2Vec.load(model)
    test_docs = [ x.strip().split() for x in codecs.open(test_docs, "r").readlines() ]
    
#infer test vectors
    
    output = open(output_file, "w+")
    for d in test_docs:
        output.write( ",".join([str(x) for x in m.infer_vector(d, alpha=start_alpha, steps=infer_epoch)]) )
    output.flush()
    output.close()

    output = open(output_file, "r")
    intstring = output.read()
    output.close()

    withoutcomma = intstring.split(",")

    withoutcomma = list(map(float, withoutcomma))   # convert string to float

    lis = li + withoutcomma                         # "lis" is a list containing the features


    df = pd.DataFrame(np.array(lis).reshape(1,302))     # converting the list into dataframe have 1 row and 302 columns

#-------------------------------------------------------------------------------
## Load the pickled files of the classifiers
    
    open_file = open("pickled_algos/LogisticRegression5k.pickle", "rb")
    LogisticRegression_classifier = pickle.load(open_file)
    open_file.close()
    
    prediction = LogisticRegression_classifier.predict(df)      # prediction is performed

    pred_str = np.array_str(prediction)                         # converting it into numpy array

    pred_str = ''.join(e for e in pred_str if e.isalnum())      # converting it into string

    #print(pred_str)
    #print(tweet)
    #print(filtered_sentence)

    output = open("twitter-out.txt","a")                        # store the results to be used for live streaming
    output.write(pred_str)
    output.write('\n')
    output.close()


#-------------------------------------------------------------------------------
## code for inserting records into the database
    now = datetime.datetime.now()

    k = str(now)

##            num_lines = 0
##            
##            with open("twitter-out.txt", 'r') as f:
##                for line in f:
##                    num_lines += 1
##                    
##            if num_lines == 1000:
##                conn = sqlite3.connect('database.db')
##                
##                conn.execute("INSERT INTO MiningReport (date, query, positive, negative)VALUES(?,?,?,?)",())
##                
##                conn.commit()
##                conn.close()


#-------------------------------------------------------------------------------
    
