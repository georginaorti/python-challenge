import os
import csv

csvpath2 = os.path.join('/Users/g/python-challenge/Pypoll/Resources/election_data.csv')

total = []
charles = []
diana = []
raymon = []

with open (csvpath2) as csvfile2:
    csvreader = csv.reader(csvfile2, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total.append(row[0])
        charles.append(row[2])
        diana.append(row[2])
        raymon.append(row[2])
    


print(f"Election Results")
print(f"---------------------------------")
print(f"Total Votes: {len(total)}")
print(f"Charles Casper Stockham:{len(charles('Charles Casper Stockham'))}")
print(f"Diana DeGette:{len(diana('Diana DeGette'))}")
print(f"Raymon Anthony Doane: ${len(raymon('Raymon Anthony Doane'))}")
print(f"---------------------------------")
print(f"Winner: Diana DeGette")
print(f"---------------------------------")

new_text = os.path.join('/Users/g/python-challenge/Pypoll/Financial_Analysis')

with open(new_text, "w") as file:
        file.write("Election Results")
        file.write("\n")
        file.write("---------------------------------")
        file.write("\n")
        file.write(f"Total Votes: {len(total)}")
        file.write("\n")
        file.write("---------------------------------")
        file.write("\n")
        file.write(f"Charles Casper Stockham: {len(charles('Charles Casper Stockham'))}")
        file.write("\n")
        file.write(f"Diana DeGette: {len(diana('Diana DeGette'))}")
        file.write("\n")
        file.write(f"Raymon Anthony Doane: {len(raymon('Raymon Anthony Doane'))}")
        file.write("\n")
        file.write("---------------------------------")
        file.write("\n")
        file.write("Winner: Diana DeGette")
        file.write("\n")
        file.write("---------------------------------")

