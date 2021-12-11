
# Diabetes Prediction Using Machine Learning.

A brief description of what this project does and who it's for

INTRODUCTION:-

- According to WHO, Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar. Hyperglycaemia, or raised blood sugar, is a common effect of uncontrolled diabetes and over time leads to serious damage to many of the body's systems, especially the nerves and blood vessels.

- Between 2000 and 2016, there was a 5% increase in premature mortality rates (i.e. before the age of 70) from diabetes. In high-income countries the premature mortality rate due to diabetes decreased from 2000 to 2010 but then increased in 2010-2016. In lower-middle-income countries, the premature mortality rate due to diabetes increased across both periods.

- In this project, i will do some feature analysis and try to find out the rootcauses.

Early Signs of Diabetes:-

- Hunger and fatigue. Your body converts the food you eat into glucose that your cells use for energy.

- Peeing more often and being thirstier.

- Dry mouth and itchy skin.

- Blurred vision.





## Objective Of Project

OBJECTIVE OF PROJECT:-

- To experiment with different classification methods to see which yields the highest accuracy.
- Classify whether someone has diabetes or not from given features.
- To determine which features are the most indicative of diabetes.
## Index

INDEX:-

1:- Importing Required Libraries.

2:- Loading the Dataset.

3:- Exploratory Data Analysis & Preprocessing.

(a) Understanding the dataset.

    - Head of the dataset.
    - Shape of the data set.
    - Types of columns.
    - Information about data set.
    - Summary of the data set.

(b) Data Cleaning.

    - Checking NULL values.
    - Checking for 0 value.

(c) Data Standardization.

4:-  Data Visualization.

-     Here we are going to plot :-

-     Count Plot :- To see if the dataset is balanced or not.
-     Pie Chart :- To show percentage of category.
-     Subplots :-  To see plot density of each column.
-     Histograms :- To see if data is normally distributed, skewed Or Outliers.
-     Scatter plots :- To understand relationship between any two variables.
-     Pair plot :- To create scatter plot between all the variables.
-     Heatmap :- To check the correlation between columns.

5:- Split the DataFrame into X and Y.

6:- Train Test Split.

7 :- Build ML Models.
-     1:- LogisticRegression()
-     2:- Support Vector Machine()
-     3:- GradientBoostingClassifier()
-     4:- Random Forest Classifier()

8:- Creating a Diabetes Prediction Web App.

-     MAKING A PREDICTIVE SYSTEM.
-     SAVING THE TRAINED MODEL.
-     LOADING THE SAVE MODEL.

## Dataset Content

DATASET CONTENT:-

- Diabetes dataset consists of several medical parameters and one dependent (outcome) parameter of binary values.
- This dataset is mainly for female gender and description of dataset is as following:-​
- 9 columns with 8 independent parameter and one outcome parameter with uniquely identified 768 observations having 268 positive for diabetes (1) and 500 negative for diabetes (0).​
-     Pregnancies : Number of times pregnant.​

-     Glucose: Oral Glucose Tolerance Test result.

- The glucose tolerance test is a lab test to check how your body moves sugar from the blood into tissues like muscle and fat.​​
-     BloodPressure: Diastolic Blood Pressure values in (mm Hg).​

- The diastolic reading, or the bottom number, is the pressure in the arteries when the heart rests between beats. This is the time when the heart fills with blood and gets oxygen.
- This is what your diastolic blood pressure number means:
- Normal: Lower than 80.
- Stage 1 hypertension: 80–89.
- Stage 2 hypertension: 90 or more.
- Hypertensive crisis: 120 or more.
- Most people with diabetes will eventually have high blood pressure.​​

-     SkinThickness: Triceps skin fold thickness in (mm).

- Skinfold thickness, so that a prediction of the total amount of body fat can be made. The triceps skinfold is necessary for calculating the upper arm muscle circumference. Its thickness gives information about the fat reserves of the body, whereas the calculated muscle mass gives information about the protein reserves.

- For adults, the standard normal values for triceps skinfolds are 2.5mm (men) or about 20% fat; 18.0mm (women) or about 30% fat. Measurement half, or less, of these values represent about the 15th percentile and can be considered as either borderline, or fat depleted. Values over 20mm (men) and 30mm (women) represent about the 85th percentile, and can be considered.​​

-     Insulin: 2-Hour serum insulin (mu U/ml).
- Insulin is a hormone that helps move blood sugar, known as glucose, from your bloodstream into your cells.
- 2-hour Serum Insulin: Greater than 150 mu U/ml relates to insulin therapy.
- Insulin therapy is a critical part of treatment for people with type 1 diabetes and also for many with type 2 diabetes. - The goal of insulin therapy is to keep your blood sugar levels within a target range.​​
-     BMI: Body mass index.
- The Body Mass Index (BMI) provides a simple, yet accurate method of assessing whether a patient is at risk from either over-or-underweight. However, a proportionally greater lean body mass and/or skeletal frame size can contribute to apparent excess body weight. Many athletes, for example would be considered ‘overweight’, yet skin-fold tests show a sub-normal amount of adipose tissue. It can easily be calculated by dividing the patient’s weight (kg) by the square of their height (meters).​
- BMI= weight(kg)/[height(m)]²​​
-     DiabetesPedigreeFunction: Diabetes pedigree function.
- Diabetes Pedigree Function, it provided some data on diabetes mellitus history in relatives and the genetic relationship of those relatives to the patient. This measure of genetic influence gave us an idea of the hereditary risk one might have with the onset of diabetes mellitus.​
-     Age - Age (years).

RESPONSE:-

-     Target - Class variable (0 or 1), 0 means No Diabeties, 1 means Diabeties.
## Lessons Learned


1:- Handling imbalanced dataset.

2:-  Using different model to find the best fit model for it.

3:-  Outliers are unusual values in your dataset, and they can distort statistical analyses and violate their assumptions. Hence it is of utmost importance to deal with them. In this case removing outliers can cause data loss.
## Conclusion

- We select the Random Forest Classifier as the right model due to high accuracy.
- Random Forest Classifier showed an improved performance was because of the presence of outlier, as we all study that Random Forest is not a distance based algorithm, thats why it is not much get affected by outliers.
- Thats why distance based algorithm such as Logistic Regression and Support Vector Showed a lower performance.
      
      - Feature Importances:-
      1. Glucose is the most important factor in the dataset of diabetes(As Glucose is highly correlated with Target).
      2. BMI and Age is also highly correlated with target.
      3. Other features such as Diabetes Pedigree Fucntion, Pregnancies, Blood Pressure, Skin Thickness and Insulin also
      contributes to the prediction.

- We now come to end of the project.
## Deployment

To deploy this project run

```bash
  streamlit run "D:\ML PROJECT\Diabetes Prediction Web App.py"
```

