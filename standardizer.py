# Names of all the different vitamins, will be totaled to create Total Vitamin Density column
vitaminColumns = [
            "Vitamin A", "Vitamin B1", "Vitamin B11", "Vitamin B12",
            "Vitamin B2", "Vitamin B3", "Vitamin B5", "Vitamin B6",
            "Vitamin C", "Vitamin D", "Vitamin E", "Vitamin K"
            ]

# The densities being calculated
densities = {
            "Fat": "Fat_Density",
            "Saturated Fats": "Saturated_Fats_Density",
            "Monounsaturated Fats": "Monounsaturated_Fats_Density",
            "Polyunsaturated Fats": "Polyunsaturated_Fats_Density",
            "Carbohydrates": "Carbohydrates_Density",
            "Sugars": "Sugars_Density",
            "Protein": "Protein_Density",
            "Dietary Fiber": "Dietary_Fiber_Density",
            "Cholesterol": "Cholesterol_Density",
            "Sodium": "Sodium_Density",
            }

# Standardizes the dataset by converting every nutritional value to its density
class Standardizer:
    def __init__(self):
       pass
        
    def standardize(self, df):
        """
        Standardize the given dataframe from values to densities.
        :param df: DataFrame being standardized.
        :return: Standardized dataframe.
        """

        # Make a copy of the DataFrame
        df = df.copy()

        # Replace the 0s in the calories column with 1s, so they can be used in division
        df = df.fillna(0)
        df["Caloric Value"] = df["Caloric Value"].replace(0, 1)

        # Grab all the calories
        cal = df["Caloric Value"]

        # For every density that we need
        for item, item_density in densities.items():
            # Divide the value by the calories to calculate density
            df[item_density] = df[item] / cal

        # Create Total Vitamin Density column by summing all the vitamins then converting to density
        df["Total_Vitamin_Density"] = df[vitaminColumns].sum(axis=1) / cal

        df = df.fillna(0)

        return df