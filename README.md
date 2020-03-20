# Spoonacular Recipe Ad Targeting

#
### Project File Summary

   - <b>[README.md](README.md)</b> - a summary of all contents in this repository.
   - <b>[/Data](/Data)</b> - all data called from the Spoonacular API saved out as .csv files.
   - <b>[/Linear_Regression_Trial](/Linear_Regression_Trial)</b> - Linear regression working code (not used for the final business recommendation).
   - <b>[/Logistic_Regression_Final](/Logistic_Regression_Final)</b> - Logistic regression code.
   - <b>[/Project_Prompt](/Project_Prompt)</b> - the prompt for this project.
   - <b>[/Python_Files](/Python_Files)</b> - .py files loaded / imported in the Jupyter Notebooks.

#
### Project Members

   - <b>[Alex Cheng](https://github.com/alexwcheng)</b>
   - <b>[Nimu Sidhu](https://github.com/gksidhu)</b>

#
### Project Scenario

Total U.S. spending on food advertising was $151 billion dollars in 2018. This was a 4.1% increase from 2017. According to the New York Times, a person living in a city today sees over 5,000 ads per day, so how can we target successful ad placement in a world where food related ads are everywhere? As a business case study to address this, we work as an ads strategy consultant to businesses selling products and services related to the food industry, such as: Williams-Sonoma, KitchenAid, Blue Apron, and Hello Fresh. They are targeting <b>[Spoonacular.com](https://spoonacular.com/)</b> to run ads. Spoonacular is a popular recipe aggregating website and app for users to look up recipes by ingredient, by nutritional content, by price, and more. The <b>[Spoonacular API](https://spoonacular.com/food-api)</b> includes over 360,000 recipes as well as an open source recipe database. Our clients only want to spend money to run ads on webpages that they know people will visit a lot. In this case, without knowing how many people visited each recipe page on Spoonacular, we will use “Likes” as our proxy metric for web-traffic.

### Project Goals

   -  We want to predict if a recipe will be  "liked" a lot, to understand where to run ads.
   -  We want to build a classification model that will predict whether a recipe will be "highly liked" or not. This way, we will be able to determine where to run ads, when a new recipe is posted on Spoonacular.

#
### Methodology 

   -  Generate business application.
   -  Find and select a source of data to draw from and analyze (Spoonacular).
   -  Identify predictor and target variables to focus on.
   -  Generate criteria and call data sorted by popularity from the API.
   -  Merge all API calls into one raw dataframe, and export to CSV.
   -  Clean data as needed.
   -  Perform Exploratory Data Analysis (EDA) to investigate the data.
   -  Determine criteria for classification.
   -  Generate logistic regression model based on criteria to fit the training data.
   -  Fit additional models using Ridge and Lasso regularization to compare with "vanilla" logistic regression model.
   -  Perform hyperparameter tuning using RandomSearchCV / GridSearchCV.
   -  Test the optimized training model on the test data and evaluate score.
   -  Plot Receiver Operating Characteristic (ROC) curve and calculate AUC to evaluate model performance on test data.
   -  Create a presentation to translate findings into actionable insights for the business application. 

#
### Project Responsibilities

   -  All project responsibilities were shared equally between <b>[Alex Cheng](https://github.com/alexwcheng)</b> and <b>[Nimu Sidhu](https://github.com/gksidhu)</b>.
