import os
import csv

election_data=os.path.join("PyPoll", "Resources", "election_data.csv")

Total_Votes=[]
Charles_Casper_Stockham=[]
Diana_DeGette=[]
Raymon_Anthony_Doane=[]
Winner=[]

Total_Votes = len(election_data)
Charles_Casper_Stockham = len(row ["Candidate": "Charles Casper Stockham"] for row in election_data)
Diana_DeGette = len(row ["Candidate": "Diana DeGette"] for row in election_data)
Raymon_Anthony_Doane = len(row["Candidate": "Raymon Anthony Doane"] for row in election_data)


with open(election_data) as csv.file:
    csv.reader=csv.reader(csv.file, delimiter=",")
    for row in csv.reader:
        Total_Votes.append(row[0])
        Charles_Casper_Stockham.append(row[1])
        Diana_DeGette.append(row[2])
        Raymon_Anthony_Doane.append(row[3])
        Winner.append(row[4])
         
    print(f"Election Results")
    print(f"------------------------")
    print(f"Total Votes: {int(Total_Votes)}")
    print(f"------------------------")
    print(f"Charles Casper Stockham: {int(Charles_Casper_Stockham)}")
    print(f"Diana DeGette: {int(Diana_DeGette)}")
    print(f"Raymon Anthony Doane: {int(Raymon_Anthony_Doane)}")
    print(f"------------------------")
    print(f"Winner: Diana DeGette")
    print(f"------------------------")