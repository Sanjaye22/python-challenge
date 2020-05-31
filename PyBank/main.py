# Dependencies
import os
import csv

#Assign variables

months = []
profit_change = []
date = []

count_months = 0
total_profit = 0
prior_month_profit = 0
current_month_profit = 0
monthly_change = 0

#Set path for file
csvpath= "C:/Users/sanja/python-challenge/PyBank/Resources/budget_data.csv"

#Open and read CSV 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this part if there is no header)
    csvheader = next(csvreader)
   
# Conducting the ask
    for row in csvreader:
        #Total months
        count_months += 1

        #Calculate total Profit/Losses
        current_month_profit = int(row[1])
        total_profit += current_month_profit

        if(count_months == 1):
            #make the value of previous month to equal to the current month
            prior_month_profit = current_month_profit              
        else:
            #compute change in profit loss
            monthly_change = current_month_profit - prior_month_profit
            
             #Append each month to the months []   
            months.append(row[0])   
            
            #Append each profit change
            profit_change.append(monthly_change) 
            
            # Make current month profit to be prior month profit 
            prior_month_profit = current_month_profit
            
            #Calculate average of changes in Profit/Losses 
            sum_profit_change = sum(profit_change) 
            average_change = round(sum_profit_change/(count_months-1), 2)

            #Greatest Increase change in profits and corresponding dates
            #Append date
            date.append(row[0])
            
            greatest_increase_profits = max(profit_change)
            greatest_decrease_profits = min(profit_change)

            increase_date = date[profit_change.index(greatest_increase_profits)]
            decrease_date = date[profit_change.index(greatest_decrease_profits)]         
   
#Print Analysis to the terminal
    print("Financial Analysis")

    print("----------------------------")

    print(f"Total Months: {count_months}")
    print(f"Total: {total_profit}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {increase_date} ({greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date} ({greatest_decrease_profits})")
  
#Export results in a text file
PyBank_Results = "C:/Users/sanja/python-challenge/PyBank/Analysis/PyBank_Results.txt"
with open(PyBank_Results, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total: {total_profit}\n")
    outfile.write(f"Average Change: {average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {increase_date} ({greatest_increase_profits})\n")
    outfile.write(f"Greatest Decrease in Profits: {decrease_date} ({greatest_decrease_profits})\n")
  


    


