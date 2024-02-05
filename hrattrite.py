import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing


# Load the pre-trained model
loaded_model = pickle.load(open('model.sav', 'rb')) 
#model = load_model('model.sav')

# Function to make predictions
def prediction(attrite):
     # Convert the input list to a DataFrame
    df = pd.DataFrame(attrite)
    # Label encode categorical variables
    label = preprocessing.LabelEncoder()
    data = [1, 3, 6, 10, 14, 16, 20, 21]
    for i in data : 
        df.iloc[i] = label.fit_transform(df.iloc[i])

        # Reshape the data for prediction
    num_data = df.values.reshape(1, -1)
    
    # Make predictions
    pred = loaded_model.predict(num_data) 

    # Return the prediction result
    if pred[0] == 0:
        return "Employee is satisfied"
    else:
        return "Employee is not satisfied"
    
    '''data = [2, 4, 7, 11, 15, 17, 21, 22]
    df.iloc[2] = label.fit_transform(df.iloc[2])
    df.iloc[4] = label.fit_transform(df.iloc[4])
    df.iloc[7] = label.fit_transform(df.iloc[7])
    df.iloc[11] = label.fit_transform(df.iloc[11])
    df.iloc[15] = label.fit_transform(df.iloc[15])
    df.iloc[17] = label.fit_transform(df.iloc[17])
    df.iloc[21] = label.fit_transform(df.iloc[21])
    df.iloc[22] = label.fit_transform(df.iloc[22])

'''
# Streamlit UI
def main():
       
    st.title("Prediction Employee Attrition in a organization")

    # Input fields for user to provide employee information
    Age = st.number_input("Age of employee")
    BusinessTravel = st.text_input("How was your  Business travel rate")
    DailyRate = st.number_input("Daily Attrition Rate")
    Department =st.text_input("Department of Attrition")             
    DistanceFromHome = st.number_input("What is the distance Level from home")
    Education = st.number_input("Highest level of education")                  
    EducationField=st.text_input("Education field of employee attrition")            
    EmployeeCount=st.number_input("Employee attrition count")               
    EmployeeNumber = st.number_input("What is the Employee Number")             
    EnvironmentSatisfaction = st.number_input("What is the Environment Satisfaction")
    Gender =st.text_input("Sex of Employee")
    HourlyRate= st.number_input("What is the Hourly Rate")                  
    JobInvolvement= st.number_input("Level of Job Involvement")             
    JobLevel = st.number_input("What is the Job Level")                    
    JobRole = st.text_input("Job Role of Employee")
    JobSatisfaction =st.number_input("What is the Job Satisfaction rate")        
    MaritalStatus =st.text_input("Marital Status of Employee")
    MonthlyIncome = st.number_input("What is the Monthly Income")             
    MonthlyRate = st.number_input("What is the Monthly Rate of Attrition")                
    NumCompaniesWorked = st.number_input("What is the Number of Companies Worked")
    Over18 =st.text_input("Employee above 18")                     
    OverTime =st.text_input("Employee doing over time")                  
    PercentSalaryHike = st.number_input("What is the Percentage of Salary Hike")            
    PerformanceRating = st.number_input("What is the Performance Rate")            
    RelationshipSatisfaction = st.text_input("What is the Relationship Satisfaction of Employee")     
    StandardHours  = st.number_input("What is the Standard Working Hours of the employee")               
    StockOptionLevel = st.number_input("What is the Stock Option Level of the Employee")            
    TotalWorkingYears   = st.number_input("What is the Total Working Years of the Employee")          
    TrainingTimesLastYear = st.number_input("What is the number of training times Last Year")        
    WorkLifeBalance = st.number_input("What is the level of Work Life Balance")
    YearsAtCompany =st.number_input("Numbers of year with the Company")
    YearsInCurrentRole =st.number_input("Numbers of year in the the Current Role")
    YearsSinceLastPromotion = st.number_input("Numbers of year last promoted")
    YearsWithCurrManager = st.number_input("Numbers of year with the current Manager")      


    # Button to trigger prediction

    Attrition = " "

    if st.button("Result"):
            Attrition = prediction([Age, BusinessTravel, DailyRate, Department,
        DistanceFromHome, Education, EducationField, EmployeeCount,
        EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate,
        JobInvolvement, JobLevel, JobRole, JobSatisfaction,
        MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked,
        Over18, OverTime, PercentSalaryHike, PerformanceRating,
        RelationshipSatisfaction, StandardHours, StockOptionLevel,
        TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance,
        YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion,
        YearsWithCurrManager])
            
        
    # Display the prediction result  
    st.success(Attrition)

if __name__ == "__main__":
    main()



     
     
     
     