import os
import csv

csvpath = os.path.join('/Users/g/python-challenge/PyBank/Pybank/Resources/budget_data.csv')

total_months = []
Profit = []
average = []


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        Profit.append(int(row[1]))

    for i in range(len(Profit)-1):
        average.append(Profit[i+1]-Profit[i])

great_increase = max(average)
great_decrease = min(average)


print(f"Financial Analysis")
print(f"---------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(Profit)}")
print(f"Average Change: {round(sum(average)/len(average),2)}")
print(f"Greatest Increase in Profits: ${str(great_increase)}")
print(f"Greatest Decrease in Profits: ${str(great_decrease)}")


new_file = os.path.join('/Users/g/python-challenge/PyBank/Pybank/Financial_Analysis')

with open(new_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(Profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(average)/len(average),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: ${str(great_increase)}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: ${str(great_decrease)}")































