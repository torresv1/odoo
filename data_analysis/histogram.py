'''
Name:       Histogram Employees Survey
Purpose:    Analyzing data from a file of survey responses from employees and presenting in a histogram
Date:       09/18/2014 11:57 PM
Author:     Vladimir Torres-Rivas
'''

#Import libraries

import pandas as pd

import matplotlib.pyplot as plt

# Read from the file.

path = r'C:/Users/torresv1/Google Drive/Personal/Education/Rutgers/Courses/Business Forecasting/Homework/'

survey = pd.read_csv( path + 'Typical_Employee_Survey_Data.csv', header = 0, keep_default_na = True, low_memory = False )

#Build the chart

satisfaction = survey['satisfaction'].value_counts()
ax = satisfaction.plot(kind='bar')
ax.set_xlim(right=4)
ax.set_title ('Results from an Employees Satisfaction Survey. Sample = 122')
ax.set_xlabel('Satisfaction Level')
ax.set_ylabel('# of Participants')
ax.set_xticklabels(('Very Satisfied','Satisfied','Dissatisfied','Very Dissatisfied'),rotation =0)
fig = ax.get_figure()
plt.show() 








