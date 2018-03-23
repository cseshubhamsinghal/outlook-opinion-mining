# outlook-opinion-mining
Opinion Mining and Sentiment Analysis


# OBJECTIVE
The objective of this project is to develop an application in order to perform sentiment
analysis on the tweets using more than one classifier and based on the classifier with
maximum accuracy, segregate them as positive, negative and neutral. Thereby, justify the
action to be taken in the future as per the mined opinion and sentiments analyzed.


# METHODOLOGY

Retrieving tweets for a particular topic:
- Application prompts the user to input the keyword (ex. Donald Trump, Iphone X, etc.) into the GUI provided for which the tweets need to be fetched.
- Tweets are fetched with the help of Listener function which is interfaced with the Twitter website using access tokens.
 
Preprocessing the tweets :
- Here preprocessing refers to tokenization, stop words removal, cleaning, Part Of Speech Tagging, Lemmatizing and stemming, etc. 
- In order to perform various symbolic and statistical Natural Language Processing, all these above tasks are performed.

Modeling of Feature Vector:
- Compiling feature lists of words from positive reviews and words from the negative reviews to hopefully see trends in specific types of words in positive or negative views.
Finding vectors of each tweet using Doc2Vec algorithm with the default value of vector size to be equal to 300, i.e. 300  vectors for each tweet are created.

Train the classifier on the dataset created and features extracted:
- Defining the classifiers (Logistic Regression, Support Vector Machine Classifier, etc.) and training the classifier on the dataset and feature extracted for each tweet in the dataset, and  determining their accuracies.
- Based on the classifier with maximum accuracy,  tweets will be classified as per the sentiments analyzed.

Representation and storage:
- Live streaming of each tweet as per the sentiments analyzed  on the two dimensional graph with tweets on x-axis and opinion on y-axis.
- Store the conclusion of the most recent results in the database.
