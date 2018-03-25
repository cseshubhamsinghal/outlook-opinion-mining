#----------------------------------------------------------------------
## import the packages

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import csv

#----------------------------------------------------------------------
## preprocessing each row of csv file

def preprocess(roww):
    stop_words = set(stopwords.words('english'))                # stopwords removal
    
    word_tokens = word_tokenize(roww)                           # tokenization

    lemmatizer = WordNetLemmatizer()                            # lemmatization

    ps = PorterStemmer()                                        # stemming

    allowed_word_types = ['WP','JJ','JJR','JJS','NN','CD']      # part of speech tagging
    
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
            
    ff = open("negcount.csv","a")

    ff.write(str(count))
    ff.write("\n")

    ff.close()
    fo.close()


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
            
    f2 = open("poscount.csv","a")

    f2.write(str(count1))
    f2.write("\n")

    f2.close()
    f1.close()  

#----------------------------------------------------------------------
## Reading each row of the csv file

def csv_reader(file_obj):

    reader = csv.reader(file_obj)
    for row in reader:
        roww=row[0]
        preprocess(roww)
        

#----------------------------------------------------------------------
## This is the main() function
        
if __name__ == "__main__":
    csv_path = "dataset.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
