import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

fifa_file=r'C:\Users\fehin\personal_projects\FIFA_21_Dataset\fifa21 raw data v2.csv'
df=pd.read_csv(fifa_file)

"""Data exploration"""
df.columns #To check the columns
df.info() #To check for missing values
df.describe() #Statistics summary

"""Task 1: To convert height and weight comlumns to numerical forms by defining a function that converts inches to cm"""

# Convert height column to numeric
# Function to convert feet and inches to centimeters
def feet_inches_to_cm(height):
    if 'cm' in height:
        return int(height.replace('cm', ''))
    else:
        feet, inches = height.split('\'')
        inches = inches.replace('"', '')
        return int(feet) * 30.48 + int(inches) * 2.54

# Apply the conversion function to the 'Height' column
df['Height'] = df['Height'].apply(feet_inches_to_cm)

# Function to convert weight from pounds to kilograms
def pounds_to_kg(weight):
    if 'lbs' in weight:
        return int(weight.replace('lbs', '')) * 0.453592
    else:
        return int(weight.replace('kg', ''))

# Apply the conversion function to the 'Weight' column
df['Weight'] = df['Weight'].apply(pounds_to_kg)

# To remove unnecessary newline characters from string columns
df[df.select_dtypes(['object']).columns] = df.select_dtypes(['object']).apply(lambda x: x.str.replace('\n', ''))

# To Check players with more than 10years at a club
df['Joined'] = pd.to_datetime(df['Joined'])
df['Years_at_club']=(pd.Timestamp('now')-df['Joined']).dt.days/365
players_with_more_than_10_years=df[df['Years_at_club']>10]


#To convert 'value', 'wage' and 'Release clause' to numbers
df['Value'] = df['Value'].str.replace('€', '').str.replace('K', '000').str.replace('M', '000000').astype(float)
df['Wage'] = df['Wage'].str.replace('€', '').str.replace('K', '000').str.replace('M', '000000').astype(float)
df['Release Clause'] = df['Release Clause'].str.replace('€', '').str.replace('K', '000').str.replace('M', '000000').astype(float)

#To strip star characters
df['W/F'] = df['W/F'].str.replace('★', '').astype(float)
df['SM'] = df['SM'].str.replace('★', '').astype(float)
df['IR'] = df['IR'].str.replace('★', '').astype(float)

#To scatter plot between wage and value
plt.scatter(df['Wage'],df['Value'])
plt.xlabel('Wage')
plt.ylabel('Value')
plt.title('Wage vs Value')
plt.show()