import numpy as np 
import pandas as pd 
import sys 
import os 
from consts import thresholds, feature_names

#Labels data based off given instructions 



#thresholds according to 



class Labeler: 
    def __init__(self, thresholds): 
        self.criteria = thresholds
        

#Take in a dataframe and label it accordingly with unhealthy/healthy according to given criteria. 
    def label(self, frame: pd.DataFrame) -> pd.DataFrame:
        labels = []

        cols = frame.columns.str.replace(' ', '_')
        frame.columns = cols
        for row in frame.itertuples(index=False):
            

            
            fat = getattr(row, 'Fat', 0)
            sugar = getattr(row, 'Sugar', 0)
            sodium = getattr(row, 'Sodium', 0)
            protein = getattr(row, 'Protein', 0)
            fiber = getattr(row, 'Fiber', 0)
            vitamins = 0

         
            if (
                #threshold here. 
                
            ):
                labels.append("Healthy")
            else:
                labels.append("Unhealthy")

        # Add as new column
        frame['Health_Label'] = labels
        print(f"✅ Added Health_Label column ({len(labels)} entries)")
        return frame






#lil demo main for the selections (final project -> [Files[datasets], labeler.py])
def main(): 
    path = os.path.join(os.getcwd(), "Files")
    
    p = input("Specify file.csv\n")  

    filename = f"FOOD-DATA-GROUP{p}.csv"
    
    df = pd.read_csv(os.path.join(path,filename))


    print(df.head())


    print("Columns:")
    print(df.columns)
    print("Rows:")
    print(df.index)

    #The labeler needs to be able to determine whether a given food is healthy or not. We will then use this data to train a binary classifier on supervised learning like knn, and use that to predict the user's eating habits. 

    L = Labeler(thresholds)
    df = L.label(df)

    print(df.head())


main()







