![Title_Slide](/Images/Slides/Title_Slide.png)

#
### Project File Summary

   - <b>[README.md](README.md)</b> - A summary of all contents in this repository.
   - <b>[Data](/Data)</b> - All data called from the Spoonacular API saved out as .csv files.
   - <b>[Images](/Images)</b> - Exported plots + additional graphics.
   - <b>[Linear_Regression_Trial](/Linear_Regression_Trial)</b> - Linear regression working code (not used for the final business recommendation).
   - <b>[Jupyter_Notebooks](/Jupyter_Notebooks)</b> - Logistic regression code in Jupyter Notebooks.
   - <b>[Project_Prompt](/Project_Prompt)</b> - The prompt for this project.
   - <b>[Python_Files](/Python_Files)</b> - .py files loaded / imported in the Jupyter Notebooks.

#
### Project Members

   - <b>[Alex Cheng](https://github.com/alexwcheng)</b>
   - <b>[Nimu Sidhu](https://github.com/gksidhu)</b>
   
#
### Project Responsibilities

   -  All project responsibilities were shared equally between <b>[Alex Cheng](https://github.com/alexwcheng)</b> and <b>[Nimu Sidhu](https://github.com/gksidhu)</b>.

#
### Project Scenario

Total U.S. spending on food advertising was $151 billion dollars in 2018. This was a 4.1% increase from 2017. According to the New York Times, a person living in a city today sees over 5,000 ads per day, so how can we target successful ad placement in a world where food related ads are everywhere? As a business case study to address this, we work as an ads strategy consultant to businesses selling products and services related to the food industry, such as: Williams-Sonoma, KitchenAid, Blue Apron, and Hello Fresh. They are targeting <b>[Spoonacular.com](https://spoonacular.com/)</b> to run ads. Spoonacular is a popular recipe aggregating website and app for users to look up recipes by ingredient, by nutritional content, by price, and more. The <b>[Spoonacular API](https://spoonacular.com/food-api)</b> includes over 360,000 recipes as well as an open source recipe database. Our clients only want to spend money to run ads on webpages that they know people will visit a lot. In this case, without knowing how many people visited each recipe page on Spoonacular, we will use “Likes” as our proxy metric for web-traffic.

#
### Project Goals

- We want to predict if a recipe will be  "liked" a lot, to understand where to run ads.
- We want to build a classification model that will predict whether a recipe will be "highly liked" or not. 
- This way, we will be able to determine where to run ads, when a new recipe is posted on Spoonacular.

**This is an example of a recipe webpage on Spoonacular where we WOULD want to run ads.** The recipe is very highly liked by Spoonacular users, which means that people are probably visiting this recipe page very often. Therefore, it is likely that our ad would be seen by lots of people!

![Computer_Ads_2.png](/Images/Slides/Computer_Ads_2.png)

**This is an example of a recipe webpage on Spoonacular where we WOULD NOT want to run ads.** This recipe only has 1 "Like". (Probably the person who made the recipe, honestly.) This means that people are probably not visiting this recipe page very often, so an ad on this page would not get seen very much.

![Computer_No_Ads_2.png](/Images/Slides/Computer_No_Ads_2.png)
   
# 
### Data

We used the [Spoonacular API](https://spoonacular.com/food-api/docs) to collect a dataset of **1,000 unique recipes** that have been aggregated on Spoonacular's website. Each recipe contained extensive information from nutritional content (calories, fat, vitamins, minerals, etc...) to dietary categories (paleo, vegan, whole30, etc...). A "Likes" count was also provided for each recipe. In lieu of webpage traffic, which would be ideal to predict users visiting a particular recipe's page, we decided to use "Likes" as our proxy target variable. From recipe information, we developed and/or utilized a total of 35 numerical predictors (indepedent variables) of "Likes".

#
### Data Collection Process

The Spoonacular API enforces a pagination limit of 100 recipes per request, so we made 10 requests to pull our 1,000 unique recipes. We pulled recipes sorted by popularity in descending order to ensure that we would get recipes with high "Like" counts. After all, we want to be able to predict recipes with a high "Like" count to invest in website ads. However upon exploring, we discovered that our dataset contained some recipes with low like counts as well, so we ended up having a decent distribution of recipes with both high and low like counts.

The data collection process was completed in 2 steps. First, we retrieved the 1,000 most popular recipes - which included only general info about each recipe (id, title, image, etc...). Second, we harvested recipe "ids", and made a second round of API requests using "ids" to retrieve detailed information about each recipe. Finally, all of this information was merged together into one DataFrame using recipe "id" and was exported to a .CSV file for safe keeping.

#
### Data Cleaning

In order to extract as many features as possible from the data, the Spoonacular JSON response needed to be keyed into a bit deeper to extract nutrition data and parse them into separate columns in our DataFrame. We dropped several columns that did not seem to be useful, such as the recipe source name and URL. There were also several columns where numerical data came in as the "string" datatype, and needed to be converted to the "integer" datatype in order to run aggregations.

#
### Exploratory Data Analysis

A Tableau dashboard was created to get a comprehensive understanding of the categorical and numerical data, all in one place. A static preview of this dashboard is displayed below. The fully interactive Tableau dashboard can be explored here: https://public.tableau.com/profile/alexander.cheng#!/vizhome/RecipeWebpageAds/RecipeWebpageAds
![Recipe_Webpage_Ads_Tableau_Dashboard.jpg](/Images/Recipe_Webpage_Ads_Tableau_Dashboard.jpg)

**Surprisingly, "Price" of a recipe does not seem to have a strong correlation with "Likes".** The distribution seems to be scattered and not very clear. One might initially think that a higher cost of ingredients would decrease the popularity of a recipe. 

![Price_Versus_Likes](/Images/Price_Versus_Likes.png)

**Recipe "Calorie" content does not seem to have a strong correlation with "Likes" either.** One might presume that if a recipe is high-calorie, then it might be a bit of a turn off to health-conscious people - therefore being less popular. But on the flip-side, people also really like high-calorie foods. Perhaps high-calorie comfort foods like cakes and cookies are popular simply for sheer taste and pleasure, and people don't really care about calories to like a particular recipe.

![Calories_Versus_Likes](/Images/Calories_Versus_Likes.png)

There seemed to be some multicollinearity among the predicting variables. A **collinearity heatmap** helps to visualize the strength of correlation between all predicting variables.

![Multicollinearity_Heatmap](/Images/Multicollinearity_Heatmap.png)

In the histogram of "Likes" we can see that our target variable seems to have an **exponential** distribution.

![Likes_Histogram](/Images/Likes_Histogram.png)

The cumulative distribution function (CDF) plot of "Likes" in our dataset shows a **logarithmic** relationship between "Likes" and cumulative probability. This means that recipes get rarer and rarer to find as their number of "Likes" increases.

![Likes_CDF.png](/Images/Likes_CDF.png)

#
### Data Preprocessing

Since we had lots of numerical data that is measured on different scales, it was important to standardize this data using StandardScalar. This standardization allows the model to train on a "level playing field", so that no one variable's numerical scale has an unfair advantage or disadvantage compared to the others as the model adjusts weights during training. We also used Scikit-learn to train/test split our data using a 75/25 split, which allowed us to train our model sufficiently before making predictions.

#
### Logistic Regression Model

We used the **median number of "Likes"** in our dataset as a cutoff between recipes with high "Likes" and recipes with low "Likes". The median number of "Likes" was approximately **1,300.** This helped ensure that our model trained on an even amount (50/50) of well-liked and less-liked recipes.

In developing this criteria, we assumed that our target variable (Likes) is **binary.** Of course, this target variable could be broken up into more categories than two. But for this project, binary classification gave us a clear yes/no on whether or not to invest in ads for a recipe's webpage.

To begin the modeling process, first we generated a vanilla logistic regression model using Statsmodels based on our binary classification criteria, and fit it to the training data using all 35 predicting features. We then calculated the Variance Inflation Factor (VIF) of all 35 predictors to see if there were any indications of multicollinearity. **We eliminated all variables with a VIF greater than 8.** (Note: in published literature, VIF cutoff ranges as low as 4 and as high as 10.) Next, using an initial alpha (confidence level) cutoff of 0.3, we eliminated more of these predictors. From here, VIF scores of all remaining features were less than 3, so VIF was no longer used to test for multicollinearity. 

To continue reducing predictors, we created another logistic regression model and fit our data using our reduced list of features. Using an even lower alpha cutoff value of 0.1, we performed 2 more rounds of variable reduction and found 6 statistically significant predictors, including **"number of ingredients", "time to make", "saturated fat", "sodium", "vitamin K", and "fiber".**

To compare with our "vanilla" logistic regression model made with Statsmodels, we created an another logistic regression model using Scikit-learn and implemented hyperparameter tuning using RandomizedSearchCV. We selected the best model from the tuning process, tested this "tuned" model on the test data, and evaluated its accuracy.

#
### Model Results

**Tuned Model - TRAIN DATA:**
   - Accuracy = 0.636
   
**3-Fold Cross-Validation, to ensure our model performance is not due to random chance:**
   - CV 1 - Accuracy = 0.62
   - CV 2 - Accuracy = 0.62
   - CV 3 - Accuracy = 0.648
   - This shows that our variance among these cross-validations was low.
   - This closely matches the mean accuracy (0.636) of the model.
   - So our model accuracy was probably not due to random chance.
   
**Tuned Model - TEST DATA:**
   - Accuracy = 0.664
   - This accuracy of predicting test data is very close to that of the training data.
   - This is good! We did not overfit to the training data.

To graphically evaluate model performance on test data, we plotted the "Receiver Operating Characteristic" (ROC) Curve and calculated the "Area Under the Curve" (AUC).

- Train AUC: 0.688
- Test AUC: 0.665

![ROC_Curve](/Images/ROC_Curve.png)

To deepen our understanding on model performance, we also plotted confusion matrices for model predictions on train data, and model predictions on test data.

**Confusion Matrix Results - TRAIN DATA**

![Confusion_Matrix_Train_Data](/Images/Confusion_Matrix_Train_Data.png)

- Out of 750 observations:
   - 226 recipes were predicted as a "winner" when it really was a "winner". (True Positives)
   - 124 recipes were predicted as a "winner" when it really was a "loser". (False Positives)
   - 251 recipes were predicted as a "loser" when it really was a "loser". (True Negatives)
   - 149 recipes were predicted as a "loser" when it really was a "winner". (False Negatives)
   
**Confusion Matrix Results - TEST DATA**

![Confusion_Matrix_Test_Data](/Images/Confusion_Matrix_Test_Data.png)

- Out of 250 observations:
   - 77 recipes were predicted as a "winner" when it really was a "winner". (True Positives)
   - 36 recipes were predicted as a "winner" when it really was a "loser". (False Positives)
   - 89 recipes were predicted as a "loser" when it really was a "loser". (True Negatives)
   - 48 recipes were predicted as a "loser" when it really was a "winner". (False Negatives)

#
### Conclusions

- We want to maximize the potential to predict correctly and make money.
- We want to minimize the potential to predict wrong and waste money.
- So, the **“precision”** of our model is the most important metric to consider.
   - Precision = Number Of Good Investments / Total Number Of Investments
   - Precision = True Positives / (True Positives + False Positives)
   - Precision = 77 / (77 + 36) = **68.1%**

**RECOMMENDATION: With a precision of 68.1% on our test data, for every 3 ads invested, 2 ads will be a good investment and 1 ad may be a loss. With these odds, we recommend that our clients follow the model to invest in ads on Spoonacular!**

#
### Future Work

- If possible, it would be better to obtain web-traffic metrics instead of using “Likes" as a proxy.
- It would help to pull more data (a greater number of recipes) from the Spoonacular database.
- Natural Language Processing may be useful to cluster text such as ingredient types - such as to predict the most visited recipe webpages with respect to the use of "avocado".
