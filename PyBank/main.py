# Script for PyBank analysis

import os
import csv

csvpath = os.path.join('budget_data.csv').replace("\\","/")

final_profit = []
profit = []
monthly_changes= []
date = []
# Initialize the variables as required.
 
count = 0
total_profit = 0
total_change_profits = 0
monthly_change_profits = 0
initial_profit = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
  
    # Conducting the ask
    for row in csvreader:    
    
      count = count +1
      # the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits from month to month. Then calulate the average change in profits
      final_profit = int(row[1])

      monthly_change_profits = final_profit- initial_profit

      #Store these monthly changes in a list    
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit


      #Calculate the average change in profits
      average_change_profits = (total_change_profits/count)

               
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
     
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {count}")
    print(f"Total Profits: {total_profit}")
    print(f"Average Change: {average_change_profits}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})")
    

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")




#The net total amount of "Profit/Losses" over the entire period


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes





