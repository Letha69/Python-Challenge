import os
import csv

csvpath= os.path.join('PyPoll\Resources\election_data.csv').replace("\\","/")

import os
import csv

poll_data = os.path.join('Resources', 'election_data.csv').replace("\\","/")

# Declare Variables
total_votes = 0

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open (poll_data, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)


    for row in csvreader:
        #Count the unique voter ID's and store in variable total_votes
        total_votes += 1

    # If candidate is found, count the times it appears and store in a list  

        if  row[2] == "Khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        else:
            otooley_votes +=1
        
            
    
 # make the dictionarie
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]
# zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictiionary
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"----------------------------")
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Output files
# Assign output file location and with the pathlib library
#output_file = Path("Election_results_Summary.txt")

# Write methods to print to Elections_Results_Summary
with open("election_results_summary.txt", "w") as text:
    text.write(f"Election Results")
    text.write("\n")
    text.write(f"----------------------------")
    text.write("\n")
    text.write(f"Total Votes: {total_votes}")
    text.write("\n")
    text.write(f"----------------------------")
    text.write("\n")
    text.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    text.write("\n")
    text.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    text.write("\n")
    text.write(f"Li: {li_percent:.3f}% ({li_votes})")
    text.write("\n")
    text.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    text.write("\n")
    text.write(f"----------------------------")
    text.write("\n")
    text.write(f"Winner: {key}")
    text.write("\n")
    text.write(f"----------------------------")



        





