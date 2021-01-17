# Script for PyBank analysis

import os

# Module for reading CSV files
import csv

csvpath = os.path.join('PYBANK', 'budget_data.csv').replace("\\","/")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    




# The total number of months included in the dataset


#The net total amount of "Profit/Losses" over the entire period


#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period