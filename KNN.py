import sys 
import os 
import pandas as pd 
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import (accuracy_score, f1_score, precision_score, recall_score,
                             confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay)
import matplotlib.pyplot as plt


#WRAPPER CLASS FOR KNN MODEL

class KNN: 
    def __init__(self, k): 
        self.k = k 
        self.model = KNeighborsClassifier(n_neighbors = k)


    def train(self,features, ftargets): 
        self.model.fit(features,ftargets)


    def predict(self, xtest): 
        predictions = self.model.predict(xtest) 
        return predictions

    def performance_metrics(self, ytest, predictions):
        return (accuracy_score(ytest, predictions),
                f1_score(ytest, predictions, pos_label="Healthy"),
                precision_score(ytest, predictions, pos_label="Healthy"),
                recall_score(ytest, predictions, pos_label="Healthy"))

    def confusion_matrix(self, ytest, predictions):
        cm = confusion_matrix(ytest, predictions, labels=["Unhealthy", "Healthy"])
        print(f"Confusion Matrix:\n {cm}")
        cm_disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Unhealthy", "Healthy"])
        cm_disp.plot()
        plt.title("k-NN")
        plt.show()

    def roc_curve(self, xtest, ytest):
        # Get predicted probabilities for positive class
        y_probabilities = self.model.predict_proba(xtest)
        y_probabilities = y_probabilities[:, 0]

        RocCurveDisplay.from_predictions(ytest, y_probabilities, pos_label="Healthy")
        plt.plot([0, 1], [0, 1], linestyle='--')
        plt.title("k-NN")
        plt.show()
    


    