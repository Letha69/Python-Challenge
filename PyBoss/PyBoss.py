import os
import csv

csvpath = os.path.join('..', 'employee_data.csv').replace("\\","/")

first_name= []
last_name= []
dob_ymd= []
dob_mdy= []
ssn= []
ssn_hedden= []
state =[]
state2 =[]
emp_id =[]


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

for row in csvreader:    
      #  The total number of months included in the dataset 
    emp_id.append(row[0])