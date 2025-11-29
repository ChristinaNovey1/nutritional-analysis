import sys 
import os 
import numpy as np 
import pandas as pd 
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score
class NN: 
    def __init__(self, features, target): 
        self.model = MLPClassifier(hidden_layer_sizes=(5,5,5), activation= 'logistic', solver='sgd', max_iter=1000,random_state=42)

    def train(self,features,target_train): 
        self.model.fit(features, target_train)
        return self.model 
    

    def predict(self, xtest):

        predictions = self.model.test(xtest)
        return predictions
    
    def accuracy(self, predictions, ytest): 
        return accuracy_score(ytest, predictions)
    



