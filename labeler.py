import pandas as pd

#Labels data based off given instructions *criteria
class Labeler: 
    def __init__(self, thresholds : dict):
        """Constructor to initialize the thresholds of the labeler."""
        self.criteria = thresholds

    def label(self, frame: pd.DataFrame) -> pd.DataFrame:
        """
        Take in a dataframe and label it accordingly with unhealthy/healthy according to given criteria.
        :param frame: The DataFrame to label
        :return: A copy of the DataFrame with the health labels included
        """

        labels = []
        scores = []

        # For every row in the DataFrame
        for row in frame.itertuples(index=False):
            # Grab the features of the current observation
            fat = getattr(row, "Fat_Density", 0)
            sat_fat = getattr(row, "Saturated_Fats_Density", 0)
            mon_fat = getattr(row, "Monounsaturated_Fats_Density", 0)
            poly_fat = getattr(row, "Polyunsaturated_Fats_Density", 0)
            carbs = getattr(row, "Carbohydrates_Density", 0)
            sugars = getattr(row, "Sugars_Density", 0)
            protein = getattr(row, "Protein_Density", 0)
            fiber = getattr(row, "Dietary_Fiber_Density", 0)
            cholesterol = getattr(row, "Cholesterol_Density", 0)
            sodium = getattr(row, "Sodium_Density", 0)
            total_vitamin = getattr(row, "Total_Vitamin_Density", 0)

            # Copy all the feature to the new row
            vals = [getattr(row,f'food'), fat,sat_fat, mon_fat,poly_fat,carbs,sugars,protein,fiber,cholesterol,sodium, total_vitamin]

            # Calculate the health score and whether healthy/unhealthy
            res, score = self.test(vals)

            if (res):
                labels.append("Healthy")
            else:
                labels.append("Unhealthy")

            scores.append(score)

        # Add the labels and scores as new columns to the DataFrame
        frame['Health_Label'] = labels
        frame['Health_Score'] = scores

        return frame

    def test(self, values) ->  {bool,int}:
        """
        Tests each nutritional value to see if it meets the thresholds and calculates
        a health score based on the thresholds it does or doesn't meet.
        :param values: The values to test whether they meet the thresholds
        :return: Boolean value representing whether the current observation
        is healthy or not, and the health score
        """

        i = 1
        score = 0

        # The categories being tested
        test_order = [
            "Fat_Density",
            "Saturated_Fats_Density",
            "Monounsaturated_Fats_Density",
            "Polyunsaturated_Fats_Density",
            "Carbohydrates_Density",
            "Sugars_Density",
            "Protein_Density",
            "Dietary_Fiber_Density",
            "Cholesterol_Density",
            "Sodium_Density",
            "Total_Vitamin_Density"
        ]

        # For every category being tested
        for test in test_order:
            # Grab the current value to test
            v = values[i]

            # Grab the current threshold
            thresh = self.criteria[test]

            # Get the operation of < or > from the threshold
            op = thresh[0]

            # Grab the value of the threshold
            val = thresh[1]

            # Check operation
            if op == '<':
                # If it meets the threshold, add to health score
                if (v < val):
                    score += thresh[2]
                # Doesn't meet threshold, penalize by deducting from health score
                else:
                    score -= thresh[3]
            elif op == '>':
                # If it meets the threshold, add to health score
                if (v > val):
                    score += thresh[2]
                # Doesn't meet threshold, penalize by deducting from health score
                else:
                    score -= thresh[3]

            i+=1

        # Check if it hits the minimum score required to be healthy (3 is the cutoff)
        res = score >= 3 
        return res,score
