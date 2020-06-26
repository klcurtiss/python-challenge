#import the csv file
import os
import csv
#set path to the csv file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("../PyBankResources", "budget_data.csv")
#set/initialize variables
totalmonths = 0
netprofit = 0
previousprofit = 0
monthlychange = 0
changelist = []
avgchngprofit = 0
maxinc = 0
maxincmonth = ""
maxdec = 0
maxdecmonth = ""

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read first row as header
    csv_header = next(csvreader)
    
#For each row after the header
    for row in csvreader:
        totalmonths = totalmonths + 1 
        netprofit = netprofit + int(row[1])
        monthlychange = int(row[1]) - previousprofit
        previousprofit = int(row[1])
        #Calculate average change in profit
        changelist.append(monthlychange)
        avgchngprofit = sum(changelist)/len(changelist)
        maxinc = max(changelist)
        if maxinc == monthlychange:
            maxincmonth = row[0]
        maxdec = min(changelist)
        if maxdec == monthlychange:
            maxdecmonth = row[0]

print("Financial Analysis")
print("------------------------------------")
print("Total Months: " +str(totalmonths))
print("Net Total Profit/Loss: " +str(netprofit))
print("Average Change in Profit/Losses: " +str(avgchngprofit))        
print("Greatest Profit Increase: " +str(maxinc))
print(maxincmonth)
print("Greatest Profit Decrease: " + str(maxdec))
print(maxdecmonth)
#print(changelist)
#print(sum(changelist))
#print(len(changelist))

f = open("Text_Financial_Analysis.txt", "w")
f.write("Finacial Analysis" + "\n")
f.write("Total Months: " +str(totalmonths)+ "\n")
f.write("Net Total Profit/Loss: " +str(netprofit) + "\n")
f.write("Average Change in Profit/Losses: " +str(avgchngprofit) + "\n")
f.write("Greatest Profit Increase: " +str(maxinc) + "\n")
f.write(maxincmonth + "\n")
f.write("Greatest Profit Decrease: " + str(maxdec) + "\n")
f.write(maxdecmonth)