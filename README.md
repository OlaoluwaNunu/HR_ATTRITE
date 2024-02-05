# HR_ATTRITE


This project on Attrition predicting employee attrition in an organization using a Random Forest Classifier. Here's a step-by-step explanation of the code and the project:
## Introduction:
The project aims to predict employee attrition using a supervised learning classification approach. This involves utilizing historical data on employees, such as their job roles, satisfaction levels, and tenure, to train a machine learning model that can predict whether an employee is likely to leave the organization.

## Data Collection:
Data is loaded from a CSV file named "HR_Employee_Attrition.csv" using the Pandas library. This dataset likely contains various features related to employees, including both numerical and categorical variables.


## Exploratory Data Analysis (EDA):
The EDA section is crucial for understanding the dataset's structure and gaining insights into potential factors influencing attrition. Some key steps include:
Checking the first and last 5 rows of the dataset.
Exploring data types, non-null counts, statistical summaries, duplicate entries, and missing values.
Visualizing the distribution of different features through histograms and bar plots.


## Label Encoding:
Since machine learning models generally require numerical input, categorical variables are converted to numerical format using Label Encoding. This preprocessing step ensures that the data is suitable for training the Random Forest Classifier.


## Splitting into Feature Variables and Labels:
The dataset is split into feature variables (X) and the target variable (y). Features represent the input variables used for predictions, and the target variable is what the model aims to predict (employee attrition in this case).

 
 ## Training the Model:
The Random Forest Classifier, a powerful ensemble learning algorithm, is employed for training the model. The dataset is split into training and testing sets to assess the model's performance on unseen data.


## Model Evaluation:
The model's performance is evaluated using the classification report, which includes metrics such as precision, recall, and F1-score for both classes (Attrition: 0 and 1). These metrics provide a comprehensive understanding of the model's ability to correctly classify instances of attrition.


## Saving the Model:
The trained Random Forest model is saved using the pickle module as a file named 'model.sav'. This allows for easy deployment and reuse of the model for future predictions.


## Insights from EDA:
The EDA visualizations provide valuable insights into potential factors contributing to employee attrition:

**Job Level**: Employees at different job levels may have varying attrition rates.

**Department**: Attrition rates vary across different departments.

**Gender**: Differences in attrition rates between genders may exist.

**Education Field**: The type of education field may influence attrition rates.

**Years at Company**: Tenure seems to be a factor, with potential differences in attrition based on the number of years an employee has been with the company.

**Job Role**: Variations in attrition rates across different roles.

**Job Satisfaction**: Lower job satisfaction might be associated with higher attrition.

**Marital Status**: Attrition rates may vary among different marital statuses.

**Overtime**: Working overtime might be related to different attrition rates.

## Deployment
This HR Prediction of Employee Attrition in an organization  model is deployed to Streamlit.
[HR Prediction of Employee Attrition](https://hrattrite-kvcnasei6zvfzwzfvpkshb.streamlit.app/)

## Conclusion and Suggestions:

The project concludes with a trained model that can predict employee attrition based on historical data. 
Insights from EDA can guide further analysis, feature selection, and potential interventions to reduce attrition.
Model evaluation metrics help assess the model's performance, and fine-tuning can be performed for better results.
Consider deploying the model in a production environment if accurate predictions are consistently achieved.
For a deeper analysis of factors leading to attrition, additional statistical tests, feature importance analysis, and qualitative data (e.g., surveys) could be explored.
Overall, this project provides a solid foundation for understanding and predicting employee attrition, offering actionable insights for HR and organizational management.



