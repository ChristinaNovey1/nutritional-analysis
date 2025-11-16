
feature_names = [
"ID", #0
"Unnamed: 0", #1
"Caloric Value", #2
"Fat", #3
"Saturated Fats", #4
"Monounsaturated Fats", #5
"Polyunsaturated Fats", #6
"Carbohydrates", #7
"Sugars", #8
"Protein", #9
"Dietary Fiber", #10
"Cholesterol", #11
"Sodium", #12
"Water", #13
"Vitamin A", #14
"Vitamin B1", #15
"Vitamin B11", #16
"Vitamin B12", #17
"Vitamin B2", #18
"Vitamin B3", #19
"Vitamin B5", #20
"Vitamin B6", #21
"Vitamin C", #22
"Vitamin D", #23
"Vitamin E", #24
"Vitamin K", #25
"Calcium", #26
"Copper", #27
"Iron", #28
"Magnesium", #29
"Manganese", #30
"Phosphorus", #31
"Potassium", #32
"Selenium", #33
"Zinc" #34
]

standardized_feature_names = [
    "Food", #0
    "Calories", #1
    "Fat Density", #2
    "Saturated Fats Density", #3
    "Monounsaturated Fats Density", #4
    "Polyunsaturated Fats Density", #5
    "Carbohydrates Density", #6
    "Sugars Density", #7
    "Protein Density", #8
    "Dietary Fiber Density", #9
    "Cholesterol Density", #10
    "Sodium Density", #11
    "Water Density",  #12
    "Vitamin A Density", #13
    "Vitamin B1 Density", #14
    "Vitamin B11 Density", #15
    "Vitamin B12 Density", #16
    "Vitamin B2 Density", #17
    "Vitamin B3 Density", #18
    "Vitamin B5 Density", #19
    "Vitamin B6 Density", #20
    "Vitamin C Density", #21
    "Vitamin D Density", #22
    "Vitamin E Density", #23
    "Vitamin K Density", #24
    "Calcium Density", #25
    "Copper Density", #26
    "Iron Density", #27
    "Magnesium Density", #28
    "Manganese Density", #29
    "Phosphorus Density", #30
    "Potassium Density", #31
    "Selenium Density", #32
    "Zinc Density" #33
]

thresholds = {

    "Caloric_Value":        ("<", 200, 2),
    "Fat":                  ("<", 10, 3),
    "Saturated_Fats":       ("<", 3, 4),


    "Monounsaturated_Fats": (">", 1.5, 1),
    "Polyunsaturated_Fats": (">", 0.8, 1),


    "Carbohydrates":        ("<", 30, 2),
    "Sugars":               ("<", 10, 4),

    "Protein":              (">", 6, 3),
    "Dietary_Fiber":        (">", 4, 3),


    "Cholesterol":          ("<", 75, 2),
    "Sodium":               ("<", 300, 3),
}