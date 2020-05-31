# Dependencies
import os
import csv

#Create dictionary 
candidates = {}
total_votes = 0

#Set path for file
csvpath= "C:/Users/sanja/python-challenge/PyPoll/Resources/election_data.csv"

#Open and read CSV 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

# Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
                            
        #Total votes
        total_votes += 1
                
        #Establish candidates        
        candidate = row[2]
                
        if candidate not in candidates:
            candidates[candidate] = 1
        
        else:
            candidates[candidate] += 1
                
    #Print Analysis to the terminal
    print("Election Results")

    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    for key, value in candidates.items():
        print(f"{key} : {str('{0:.3%}'.format (value /total_votes))}, ({value})")        
    print("----------------------------")
    print(f"Winner: {max(candidates, key=candidates.get)}")
    
    #Export results in a text file
PyPoll_Results = "C:/Users/sanja/python-challenge/PyPoll/Analysis/PyPoll_Results.txt"
with open(PyPoll_Results, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("----------------------------\n")
    for key, value in candidates.items():        
        outfile.write(f"{key} : {str('{0:.3%}'.format (value /total_votes))}, ({value})\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner: {max(candidates, key=candidates.get)}\n")
    outfile.write("----------------------------\n")  

        


    
    