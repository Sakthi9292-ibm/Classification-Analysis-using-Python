# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 23:39:32 2019

@author: SakthivelSundaram
"""
import pandas as pa 
data = pa.read_csv("data12.csv")


data.head()
x=data[["x1","x2","x3","x3","x4","x5","x6","x7","x8","x9","x10","x11"]]
y=data["y"]

from sklearn.model_selection import train_test_split


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.10 , random_state = 50)



# Logistic Regression 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

lr = LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
rms = sqrt(mean_squared_error(y_test, y_pred))
print("Logistic---",rms)
print(y_test[:10])
print(y_pred[:10])


#navies - Bayes
from sklearn.naive_bayes import GaussianNB

gb = GaussianNB()
gb.fit(x_train,y_train)
y_pred_gb = gb.predict(x_test)
rmse=sqrt(mean_squared_error(y_test,y_pred_gb))
print("Navie-Bayes--------",rmse)
print(y_test[:10])
print(y_pred_gb[:10])


#Decision Tree

from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier(max_depth=10,random_state=101,min_samples_leaf=5)
dtree.fit(x_train,y_train)
y_pred_tree=dtree.predict(x_test)
rmsd=sqrt(mean_squared_error(y_test,y_pred_gb))
print("Decision Tree--------",rmsd)
print(y_test[:10])
print(y_pred_tree[:10])

#Random Forest

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
rfc.fit(x_train,y_train)
y_pred_rf=rfc.predict(x_test)
rmsr=sqrt(mean_squared_error(y_test,y_pred_rf))
print("Random Forest--------",rmsr)
print(y_test[:10])
print(y_pred_rf[:10])






