import sys
import os 
import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, f1_score, precision_score, recall_score,
                             confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay)
import matplotlib.pyplot as plt

class RF: 
    def __init__(self): 
        self.model = RandomForestClassifier(n_estimators=60, max_depth=None, random_state=42) #Maybe we need tro switch the n estimators here. 

    def train(self, xtrain, ytrain): 
        self.model.fit(xtrain, ytrain)
    
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
        plt.title("Random Forest")
        plt.show()

    def roc_curve(self, xtest, ytest):
        # Get predicted probabilities for positive class
        y_probabilities = self.model.predict_proba(xtest)
        y_probabilities = y_probabilities[:, 0]

        RocCurveDisplay.from_predictions(ytest, y_probabilities, pos_label="Healthy")
        plt.plot([0, 1], [0, 1], linestyle='--')
        plt.title("Random Forest")
        plt.show()
    