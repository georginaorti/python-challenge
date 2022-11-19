import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

Total_Months= []
Total=[]
Average_Change=[]
Greatest_Increase_in_Profits=[]
Greatest_Decrease_in_Profits=[]

Total_Months = len(budget_data)
Total = sum(row['Profit/Losses'] for row in budget_data)
Average_Change = round(Total/Total_Months)
Greatest_Increase_in_Profits = max(budget_data)
Greatest_Decrease_in_Profits = min(budget_data)


with open(budget_data) as csv.file:
    csv.reader= csv.reader(csv.file, delimiter=",")
    for row in csv.reader:
        Total_Months.append(row[0])
        Total.append(row[1])
        Average_Change.append(row[2])
        Greatest_Increase_in_Profits.append(row[3])
        Greatest_Decrease_in_Profits.append(row[4])


    print(f"Financial Analysis")
    print(f"---------------------------------")
    print(f"Total Months: {int(Total_Months)}")
    print(f"Total: {int(Total)}")
    print(f"Average Change: {int(Average_Change)}")
    print(f"Greatest Increase in Profits: {str(Greatest_Increase_in_Profits)}")
    print(f"Greatest Decrease in Profits: {str(Greatest_Decrease_in_Profits)}")    