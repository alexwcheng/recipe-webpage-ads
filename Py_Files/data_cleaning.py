import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import json
%matplotlib inline

with open("/Users/flatironschooldc3/FlatironSchoolRepo/Projects/Recipes/Data/top_1000_recipes_info.json") as datafile:
  data = json.load(datafile)

for rec_list in data:
    for recipe in rec_list:
        # Add clean nutrition column
        nutrients = []
        nutrient_amts = []
        for index, val in enumerate(recipe['nutrition']['nutrients']):
            nutrient_name = recipe['nutrition']['nutrients'][index]['title']
            nutrients.append(nutrient_name)
            nutrient_amt = recipe['nutrition']['nutrients'][index]['amount']
            nutrient_amts.append(nutrient_amt)
        recipe['nutrition_info'] = dict(zip(nutrients, nutrient_amts))

        # Add num ingredients
        recipe['num_ingredients'] = len(recipe['extendedIngredients'])

columns = ['vegetarian', 'vegan', 'glutenFree', 'dairyFree', 'veryHealthy', 'cheap',
           'veryPopular', 'sustainable', 'ketogenic', 'whole30', 'aggregateLikes',
           'spoonacularScore', 'healthScore', 'pricePerServing', 'extendedIngredients',
           'id', 'title', 'readyInMinutes', 'servings', 'nutrition', 'cuisines', 'dishTypes',
           'diets', 'occasions', 'winePairing', 'instructions', 'analyzedInstructions',
           'preparationMinutes', 'cookingMinutes', 'nutrition_info',
           'num_ingredients']

df = pd.DataFrame(columns = columns)
for ind_10, val in enumerate(data):
    df_new = pd.DataFrame(data[ind_10])
    df = pd.concat([df, df_new])

df.reset_index(drop = True, inplace= True)

numbers = list(range(0,1000))
Calories = []
Fat = []
Saturated_Fat = []
Carbohydrates = []
Sugar = []
Cholesterol = []
Sodium = []
Protein = []
Vitamin_K = []
Vitamin_A = []
Vitamin_C = []
Manganese = []
Folate = []
Fiber = []
Copper = []
Magnesium = []
Phosphorus = []
Vitamin_B6 = []
Potassium = []
Vitamin_B1 = []
Iron = []
Vitamin_B2 = []
Vitamin_E = []
Zinc = []
Vitamin_B5 = []
Vitamin_B3 = []
Calcium = []
Selenium = []
for x in numbers:
    if 'Calories' in df['nutrition_info'][x]:
        Calories.append(df['nutrition_info'][x]['Calories'])
    else:
        Calories.append(0)
for x in numbers:
    if 'Fat' in df['nutrition_info'][x]:
        Fat.append(df['nutrition_info'][x]['Fat'])
    else:
        Fat.append(0)
for x in numbers:
    if 'Saturated Fat' in df['nutrition_info'][x]:
        Saturated_Fat.append(df['nutrition_info'][x]['Saturated Fat'])
    else:
        Saturated_Fat.append(0)
for x in numbers:
    if 'Carbohydrates' in df['nutrition_info'][x]:
        Carbohydrates.append(df['nutrition_info'][x]['Carbohydrates'])
    else:
        Carbohydrates.append(0)
for x in numbers:
    if 'Sugar' in df['nutrition_info'][x]:
        Sugar.append(df['nutrition_info'][x]['Sugar'])
    else:
        Sugar.append(0)
for x in numbers:
    if 'Cholesterol' in df['nutrition_info'][x]:
        Cholesterol.append(df['nutrition_info'][x]['Cholesterol'])
    else:
        Cholesterol.append(0)
for x in numbers:
    if 'Sodium' in df['nutrition_info'][x]:
        Sodium.append(df['nutrition_info'][x]['Sodium'])
    else:
        Sodium.append(0)
for x in numbers:
    if 'Protein' in df['nutrition_info'][x]:
        Protein.append(df['nutrition_info'][x]['Protein'])
    else:
        Protein.append(0)
for x in numbers:
    if 'Vitamin K' in df['nutrition_info'][x]:
        Vitamin_K.append(df['nutrition_info'][x]['Vitamin K'])
    else:
        Vitamin_K.append(0)
for x in numbers:
    if 'Vitamin A' in df['nutrition_info'][x]:
        Vitamin_A.append(df['nutrition_info'][x]['Vitamin A'])
    else:
        Vitamin_A.append(0)
for x in numbers:
    if 'Vitamin C' in df['nutrition_info'][x]:
        Vitamin_C.append(df['nutrition_info'][x]['Vitamin C'])
    else:
        Vitamin_C.append(0)
for x in numbers:
    if 'Manganese' in df['nutrition_info'][x]:
        Manganese.append(df['nutrition_info'][x]['Manganese'])
    else:
        Manganese.append(0)
for x in numbers:
    if 'Folate' in df['nutrition_info'][x]:
        Folate.append(df['nutrition_info'][x]['Folate'])
    else:
        Folate.append(0)
for x in numbers:
    if 'Fiber' in df['nutrition_info'][x]:
        Fiber.append(df['nutrition_info'][x]['Fiber'])
    else:
        Fiber.append(0)
for x in numbers:
    if 'Copper' in df['nutrition_info'][x]:
        Copper.append(df['nutrition_info'][x]['Copper'])
    else:
        Copper.append(0)
for x in numbers:
    if 'Magnesium' in df['nutrition_info'][x]:
        Magnesium.append(df['nutrition_info'][x]['Magnesium'])
    else:
        Magnesium.append(0)
for x in numbers:
    if 'Phosphorus' in df['nutrition_info'][x]:
        Phosphorus.append(df['nutrition_info'][x]['Phosphorus'])
    else:
        Phosphorus.append(0)
for x in numbers:
    if 'Vitamin B6' in df['nutrition_info'][x]:
        Vitamin_B6.append(df['nutrition_info'][x]['Vitamin B6'])
    else:
        Vitamin_B6.append(0)
for x in numbers:
    if 'Potassium' in df['nutrition_info'][x]:
        Potassium.append(df['nutrition_info'][x]['Potassium'])
    else:
        Potassium.append(0)
for x in numbers:
    if 'Vitamin B1' in df['nutrition_info'][x]:
        Vitamin_B1.append(df['nutrition_info'][x]['Vitamin B1'])
    else:
        Vitamin_B1.append(0)
for x in numbers:
    if 'Iron' in df['nutrition_info'][x]:
        Iron.append(df['nutrition_info'][x]['Iron'])
    else:
        Iron.append(0)
for x in numbers:
    if 'Vitamin B2' in df['nutrition_info'][x]:
        Vitamin_B2.append(df['nutrition_info'][x]['Vitamin B2'])
    else:
        Vitamin_B2.append(0)
for x in numbers:
    if 'Vitamin E' in df['nutrition_info'][x]:
        Vitamin_E.append(df['nutrition_info'][x]['Vitamin E'])
    else:
        Vitamin_E.append(0)
for x in numbers:
    if 'Zinc' in df['nutrition_info'][x]:
        Zinc.append(df['nutrition_info'][x]['Zinc'])
    else:
        Zinc.append(0)
for x in numbers:
    if 'Vitamin B5' in df['nutrition_info'][x]:
        Vitamin_B5.append(df['nutrition_info'][x]['Vitamin B5'])
    else:
        Vitamin_B5.append(0)
for x in numbers:
    if 'Vitamin B3' in df['nutrition_info'][x]:
        Vitamin_B3.append(df['nutrition_info'][x]['Vitamin B3'])
    else:
        Vitamin_B3.append(0)
for x in numbers:
    if 'Calcium' in df['nutrition_info'][x]:
        Calcium.append(df['nutrition_info'][x]['Calcium'])
    else:
        Calcium.append(0)
for x in numbers:
    if 'Selenium' in df['nutrition_info'][x]:
        Selenium.append(df['nutrition_info'][x]['Selenium'])
    else:
        Selenium.append(0)

df['Calories'] = Calories
df['Fat'] = Fat
df['Saturated_Fat'] = Saturated_Fat
df['Carbohydrates'] = Carbohydrates
df['Sugar'] = Sugar
df['Cholesterol'] = Cholesterol
df['Sodium'] = Sodium
df['Protein'] = Protein
df['Vitamin_K'] = Vitamin_K
df['Vitamin_A'] = Vitamin_A
df['Vitamin_C'] = Vitamin_C
df['Manganese'] = Manganese
df['Folate'] = Folate
df['Fiber'] = Fiber
df['Copper'] = Copper
df['Magnesium'] = Magnesium
df['Phosphorus'] = Phosphorus
df['Vitamin_B6'] = Vitamin_B6
df['Potassium'] = Potassium
df['Vitamin_B1'] = Vitamin_B1
df['Iron'] = Iron
df['Vitamin_B2'] = Vitamin_B2
df['Vitamin_E'] = Vitamin_E
df['Zinc'] = Zinc
df['Vitamin_B5'] = Vitamin_B5
df['Vitamin_B3'] = Vitamin_B3
df['Calcium'] = Calcium
df['Selenium'] = Selenium

df = df.drop(columns=['cuisines', 'creditsText', 'occasions', 'nutrition', 'nutrition_info',
                      'license', 'image', 'imageType', 'sourceName', 'sourceUrl', 'cheap', 'gaps', 'winePairing'])

df.to_csv('../Data/Recipes.csv')
