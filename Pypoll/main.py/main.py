import os
import csv

election_data=os.path.join("..", "Resources", "election_data.csv")

Total_Votes=[]
Charles_Casper_Stockham=[]
Diana_DeGette=[]
Raymon_Anthony_Doane=[]
Winner=[]

with open(election_data) as csv.file:
    csv.reader=csv.reader(csv.file, delimiter=",")
    for row in csv.reader:
        Total_Votes.append(row[0])
        Charles_Casper_Stockham.append(row[1])
        Diana_DeGette.append(row[2])
        Raymon_Anthony_Doane.append(row[3])
        Winner.append(row[4])
         
