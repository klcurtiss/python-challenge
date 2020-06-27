import os
import csv
#set path to the csv file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("../Resources", "election_data.csv")
#set/initialize variables
totalvotes = 0
candidateslist = []
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0
khanpercent = 0
correypercent = 0
lipercent = 0
otoolpercent = 0
winnercount = 0
winner = ""

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read first row as header
    csv_header = next(csvreader)
    #For each row after the header
    for row in csvreader:
        totalvotes = totalvotes + 1 
        if row[2] not in candidateslist:
            candidateslist.append(row[2])
        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        if row[2] == "Correy":
            correyvotes = correyvotes + 1
        if row[2] == "Li":
            livotes = livotes + 1
        if row[2] == "O'Tooley":
            otooleyvotes = otooleyvotes +1
    khanpercent = khanvotes/totalvotes * 100
    khanpercent = round(khanpercent, 3)
    correypercent = correyvotes/totalvotes * 100
    correypercent = round(correypercent, 3)
    lipercent = livotes/totalvotes * 100
    lipercent = round(lipercent, 3)
    otoolpercent = otooleyvotes/totalvotes * 100
    otoolpercent = round(otoolpercent, 3)
winnercount = max(khanvotes, correyvotes, livotes, otooleyvotes)
if winnercount == khanvotes:
    winner = "Khan"
elif winnercount == correyvotes:
    winner = "Correy"
elif winnercount == livotes:
    winner = "Li"
elif winnercount == otooleyvotes:
    winner = "O'Tooley"
    
print("Election Results")
print("-------------------------------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------------------------------")
#print(candidateslist)
print("Khan: " + str(khanpercent) + "% (" + str(khanvotes)+ ")")
print("Correy: " + str(correypercent) + "% (" + str(correyvotes) + ")")
print("Li: " + str(lipercent) + "% (" + str(livotes) + ")")
print("O'Tooley: " + str(otoolpercent) + "% (" + str(otooleyvotes) + ")")
print("-------------------------------------------------")
print("Winner: " + str(winner)) 
print("-------------------------------------------------")

f = open("Text_Poll_Results.txt", "w")
f.write("Election Results" + "\n")
f.write("Total Votes: " + str(totalvotes) + "\n")
f.write("Khan: " + str(khanpercent) + "% (" + str(khanvotes)+ ")" + "\n")
f.write("Correy: " + str(correypercent) + "% (" + str(correyvotes) + ")" + "\n")
f.write("Li: " + str(lipercent) + "% (" + str(livotes) + ")" + "\n")
f.write("O'Tooley: " + str(otoolpercent) + "% (" + str(otooleyvotes) + ")" + "\n")
f.write("Winner: " + str(winner))