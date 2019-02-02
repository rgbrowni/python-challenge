import os
import csv

vote_name = [] 

vote_tallies = []


with open('/Users/ryanbrowning/Desktop/PythonStuff/03-Python_Homework_Instructions_PyPoll_Resources_election_data copy.csv') as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
                vote_name.append(row['Candidate'])
                #print(row)
                #if count > 5:
                #        break
                count += 1

true_count = count-1

print('Election Results')

print('-------------------------')

print('Total Votes: ',true_count)

print('-------------------------')

khan_count = 0

cor_count = 0

li_count = 0

tool_count = 0

for n in range(0,true_count):
        if vote_name[n] == 'Khan':
                khan_count = khan_count + 1

for n in range(0,true_count):
        if vote_name[n] == 'Correy':
                cor_count = cor_count + 1

for n in range(0,true_count):
        if vote_name[n] == 'Li':
                li_count = li_count + 1

for n in range(0,true_count):
        if vote_name[n] == "O'Tooley":
                tool_count = tool_count + 1


vote_tallies = [khan_count, cor_count, li_count, tool_count]

khan_percent = 100*khan_count/true_count

cor_percent = 100*cor_count/true_count

li_percent = 100*li_count/true_count

tool_percent = 100*tool_count/true_count

win_index = vote_tallies.index(max(vote_tallies))

if win_index == 0:
	winner = 'Khan'

if win_index == 1:
	winner = 'Correy'

if win_index == 2:
	winner = 'Li'

if win_index == 3:
	winner = "O'Tooley"

print('Kahn: ','{:,.3f}%'.format(khan_percent), khan_count)

print('Correy: ','{:,.3f}%'.format(cor_percent), cor_count)

print('Li: ','{:,.3f}%'.format(li_percent),'(', li_count,')')

print("O'Tooley: ",'{:,.3f}%'.format(tool_percent), tool_count)

print('-------------------------')

print('Winner: ',winner)	

print('-------------------------')