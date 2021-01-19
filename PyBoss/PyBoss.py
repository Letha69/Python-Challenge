# Import Dependencies
import os
import csv

#Input file path
csvpath = os.path.join('Resources','employee_data.csv')

# List to store data

name = []
first_name= []
last_name= []
dob_ymd= []
dob_mdy= []
ssn= []
ssn_hidden= []
abbrev =[]
emp_id =[]

# Dictionary containing states names as keys and abbreviations as values (provided) 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',

    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csvpath, newline = '', encoding = 'utf-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
  header = next(csvreader)


  # Iterate through each row

  for row in csvreader:    
      #  Append variables into list
        emp_id.append(row[0])
      
        dob_ymd.append(row[2])   

      # Split full name into first and last name
        name = row[1].split(" ")
        first_name = first_name + [name[0]]     
        last_name = last_name + [name[1]]

      #Append and format DOB
        for i in dob_ymd:
            y = i.split('-')[0]
            m = i.split('-')[1]
            d = i.split('-')[2]
            dob_mdy.append(f'{m}/{d}/{y}')
            #print(dob_mdy)
      # Append and format ssn
        ssn = row[3].split("-")
        ssn_hidden.append("***-**-" + ssn[2])
      ## append  and format state
        abbrev.append(us_state_abbrev[row[4]])

      # zip lists together
        cleaned_csv = zip(emp_id, first_name, last_name, dob_mdy, ssn_hidden, abbrev)

      # set variable for output file
        output_file = os.path.join("employee_data_final.csv")

      # open the output file
with open (output_file, "w", newline ='', encoding = 'utf-8') as datafile:
  writer = csv.writer(datafile)

    # write the header row
  writer.writerow (["Emp ID","First Name","Last Name","DOB","SSN","State"])
    # write in zipped rows
  writer.writerow(cleaned_csv)


      