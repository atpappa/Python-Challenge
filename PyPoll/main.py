import csv,os

file = os.path.join('Resources','election_data.csv')

with open(file) as csv_file:
    # Store the data into a variable
    csv_reader = csv.reader(csv_file)
    # Skip the header as input
    next(csv_reader)
    row = next(csv_reader)

    #Initialize variables

    totalVotes = 0
    candidateNames = []
    candidateVotes = {}

#loop through votes and candidates
    for row in csv_reader:
        totalVotes =+ 1
        candidateName = row[2]

        if candidateName not in candidateNames:
            candidateNames.append(candidateName)
            candidateVotes[candidateName] = 0

        candidateVotes[candidateName] = candidateVotes[candidateName] + 1

#print statements
print('\n\nElection Results')
print('---------------------------')
print('Total Votes: ' + str(totalVotes))
print('---------------------------')

winningVotes = 0

#Determine winning candidate/votes for each candidate
for candidateName in candidateVotes:
    votes = candidateVotes.get(candidateName)
    votePercentage = float(votes) / float(totalVotes) * 100
    if votes > winningVotes:
        winner = candidateName
        winningVotes = votes
    voterOutput = f'{candidateName}: {round(votePercentage, 3)}% ({votes})\n'
 #   votingOutput += voterOutput 
    print(voterOutput, end="")

# Printing statement results 
print('---------------------------')
print('Winner: ' + winner)
print('---------------------------')

# Output files to a text file
file = open("results.txt", "w")
file.write("Election Results" + "\n")
file.write("---------------------------" + "\n")
file.write(f"Total Votes: {totalVotes}\n")
file.write("---------------------------" + "\n")
file.write(f"Candidates: {voterOutput}\n")
file.write("---------------------------" + "\n")
file.write(f"Winner: {winner}\n")
file.close()
