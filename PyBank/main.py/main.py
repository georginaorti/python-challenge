import os
import csv

budget_data = os.path.join('..', 'Resources', 'budget_data.csv')

Total_Months= []
Total=[]
Average_Change=[]
Greatest_Increase_in_Profits=[]
Greatest_Decrease_in_Profits=[]

with open(budget_data) as csv.file:
    csv.reader= csv.reader(csv.file, delimiter=",")
    for row in csv.reader:
        Total_Months.append(row[0])
        Total.append(row[1])
        Average_Change.append(row[2])
        Greatest_Increase_in_Profits.append(row[3])
        Greatest_Decrease_in_Profits.append(row[4])






