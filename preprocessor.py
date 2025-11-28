import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# Preprocessor class, will be used to preprocess the data for models
class Preprocessor:
    # Constructor, initializes the data attribute with the dataset that we're preprocessing
    def __init__(self, data : pd.DataFrame, columns : list):
        self.data = data
        self.columns = columns

    def preprocess(self):
        # Converting columns in mg to g
        self.data.loc[:, "sodium_g"] = self.data["sodium_mg"].div(1000, axis=0)
        self.data.loc[:, "cholesterol_g"] = self.data["cholesterol_mg"].div(1000, axis=0)

        # Grabbing the columns we need
        columns_needed = self.data[self.columns]

        # Normalizing carbs, proteins, fats, and calories by calculating how much per meal
        meal_frequencies = columns_needed["Daily meals frequency"]
        daily_nutrition = ["Carbs", "Proteins", "Fats", "Calories"]
        nutrition_per_meal = columns_needed[daily_nutrition].div(meal_frequencies, axis=0)

        # Normalizing sugar, sodium, cholesterol with serving size
        serving_sizes = columns_needed["serving_size_g"]
        nutrition = ["sugar_g", "sodium_g", "cholesterol_g"]
        nutrition_per_serving = columns_needed[nutrition].div(serving_sizes, axis=0)

        # Use one-hot encoding for categorical features (diet_type and cooking_method)
        one_hot_encoder = OneHotEncoder(sparse_output=False)
        categorical_columns = ["diet_type", "cooking_method"]
        one_hot_encoded = one_hot_encoder.fit_transform(columns_needed[categorical_columns])
        one_hot_encoded = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_columns))

        # Combine numerical features and standardize
        features = pd.DataFrame()
        features = pd.concat([features, nutrition_per_meal, nutrition_per_serving], axis=1)
        scaler = StandardScaler()
        standardized_features = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

        # Combine standardized features with one hot encoded features
        final_features = pd.DataFrame()
        final_features = pd.concat([final_features, standardized_features, one_hot_encoded], axis=1)

        return final_features
