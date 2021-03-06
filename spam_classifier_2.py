# -*- coding: utf-8 -*-
"""Spam Classifier-2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-eAFR8yhECARlDuhAbEY0r6WB5s_Sf8h
"""

#Importing libraries
import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#Importing the dataset
data=pd.read_csv('/content/SMSSpamCollection.txt',sep='\t',names=["label","message"])

data

"""##**CountVectorizer + PorterStemmer**"""

#Data Cleaning and Preprocessing
stemmer=PorterStemmer()
corpus=[]
for i in range(0, len(data)):
  review=re.sub('[^a-zA-Z]',' ',data['message'][i])
  review=review.lower()
  review=review.split()
  review=[stemmer.stem(word) for word in review if not word in stopwords.words('english')]
  review=' '.join(review)
  corpus.append(review)

corpus

#Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=5000)
x=cv.fit_transform(corpus).toarray()
x

y=pd.get_dummies(data['label'])
y=y.iloc[:,1].values
y

#Train Test Split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#Training model using Naive Bayes
from sklearn.naive_bayes import MultinomialNB
spam_detect_model1=MultinomialNB().fit(x_train,y_train)
y_pred1=spam_detect_model1.predict(x_test)
y_pred1

from sklearn.metrics import accuracy_score
a=(accuracy_score(y_test,y_pred1)*100)
a

#Training model using Support Vector Machine
from sklearn.svm import SVC
spam_detect_model2=SVC().fit(x_train,y_train)
y_pred2=spam_detect_model2.predict(x_test)
y_pred2

from sklearn.metrics import accuracy_score
a=(accuracy_score(y_test,y_pred2)*100)
a

#Training model using Random Forest
from sklearn.ensemble import RandomForestClassifier
spam_detect_model3=RandomForestClassifier().fit(x_train,y_train)
y_pred3=spam_detect_model3.predict(x_test)
y_pred3

from sklearn.metrics import accuracy_score
a=(accuracy_score(y_test,y_pred3)*100)
a

#Training model using K-Nearest Neighbour
from sklearn.neighbors import KNeighborsClassifier
spam_detect_model4=KNeighborsClassifier().fit(x_train,y_train)
y_pred4=spam_detect_model4.predict(x_test)
y_pred4

from sklearn.metrics import accuracy_score
a=(accuracy_score(y_test,y_pred4)*100)
a

#Training model using Decision Tree
from sklearn.ensemble import AdaBoostClassifier
spam_detect_model5=AdaBoostClassifier().fit(x_train,y_train)
y_pred5=spam_detect_model5.predict(x_test)
y_pred5

from sklearn.metrics import accuracy_score
a=(accuracy_score(y_test,y_pred5)*100)
a

import pickle
pickle.dump(cv,open('vectorizer.pkl','wb'))
pickle.dump(spam_detect_model1,open('model.pkl','wb'))