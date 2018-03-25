
#------------------------------------------------------------------------------------------------------------------------------------------
## import the classes of classifiers

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

#------------------------------------------------------------------------------------------------------------------------------------------
## import the class in order to save the trained classifiers as pickle file

import pickle

#------------------------------------------------------------------------------------------------------------------------------------------
## import the classes of pandas data frame and spliting of data set

import pandas as pd
#from sklearn.model_selection import train_test_split

#------------------------------------------------------------------------------------------------------------------------------------------
## import the classes for splitting the dataset into  training and testing set. Also, to stratify the dataset.

from sklearn.cross_validation import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

#------------------------------------------------------------------------------------------------------------------------------------------
## fetch the dataset.csv file

dataset_file = 'dataset.csv'
data = pd.read_csv(dataset_file)                    # convert it into pandas data frame
data = data.drop('tweets',axis=1)
#print (data.head())

y = data.label                                      # store response vector in y
X = data.drop('label', axis=1)                      # store feature matrix in x

#------------------------------------------------------------------------------------------------------------------------------------------
## splitting of dataset into 80% training set and 20% testing set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

                                                    # stratify is used to proportionately distribute the dataset into training and testing sets as per the predicted label column


##print ("\nX_train:\n")
##print(X_train.head())
##print (X_train.shape)                             # this commented part can be used to determine X_train and X_test using head and shape.
##print ("\nX_test:\n")
##print(X_test.head())
##print (X_test.shape)


##y_train.to_csv("y_train.csv")                     # this commented part can be used to determine weather stratify has been performed in the right way or not.
##y_test.to_csv("y_test.csv")

#------------------------------------------------------------------------------------------------------------------------------------------
## instantiate the model

clf1 = LogisticRegression()
#clf2 = MultinomialNB()                                     # Naive Bayes algorithm cannot be used because our dataset is having negative values.
clf3 = RandomForestClassifier()
clf4 = GradientBoostingClassifier()
clf5 = SVC()

#------------------------------------------------------------------------------------------------------------------------------------------
## fit the model with training data

clf1.fit(X_train,y_train)
#clf2.fit(X_train,y_train)
clf3.fit(X_train,y_train)
clf4.fit(X_train,y_train)
clf5.fit(X_train,y_train)

#------------------------------------------------------------------------------------------------------------------------------------------
## pickled all the classifiers

##save_classifier = open("pickled_algos/LogisticRegression5k.pickle","wb")
##pickle.dump(clf1, save_classifier)
##save_classifier.close()
##
####save_classifier = open("pickled_algos/MultinomialNB5k.pickle","wb")
####pickle.dump(clf2, save_classifier)
####save_classifier.close()
##
##save_classifier = open("pickled_algos/RandomForestClassifier5k.pickle","wb")
##pickle.dump(clf3, save_classifier)
##save_classifier.close()
##
##save_classifier = open("pickled_algos/GradientBoostingClassifier5k.pickle","wb")
##pickle.dump(clf4, save_classifier)
##save_classifier.close()
##
##save_classifier = open("pickled_algos/SVC5k.pickle","wb")
##pickle.dump(clf5, save_classifier)
##save_classifier.close()

#------------------------------------------------------------------------------------------------------------------------------------------
## predicting the response for the new observations


y_pred1 = clf1.predict(X_test)
##y_pred2 = clf2.predict(X_test)
y_pred3 = clf3.predict(X_test)
y_pred4 = clf4.predict(X_test)
y_pred5 = clf5.predict(X_test)

#------------------------------------------------------------------------------------------------------------------------------------------
## comparing actual response values (y_test) with predicted response values (y_pred) on the testing set

from sklearn import metrics

print("Logistic Regression model accuracy:", metrics.accuracy_score(y_test, y_pred1))
#print(clf1.score(X_train,y_train))                         ## This commented line gives the accuracy of the logistic regression classifier on the training set.

##print("MultinomialNBClassifier model accuracy:", metrics.accuracy_score(y_test, y_pred2))
print("RandomForestClassifier model accuracy:", metrics.accuracy_score(y_test, y_pred3))
print("GradientBoostingClassifier model accuracy:", metrics.accuracy_score(y_test, y_pred4))
print("SVCClassifier model accuracy:", metrics.accuracy_score(y_test, y_pred5))


















