import csv

month = []
profit_loss = []
change_val = []

with open('/Users/ryanbrowning/Downloads/03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv') as file:
        reader = csv.DictReader(file)
        count = 1
        for row in reader:
                month.append(row['Date'])
                profit_loss.append(row['Profit/Losses'])

sum = 0

num_months = len(month)

for n in range(0,num_months):
        sum = sum + int(profit_loss[n])

text_file = open("Output.txt", "w")
text_file.write('Total Months: ')
text_file.write(str(num_months))
text_file.write("\n")

print('Total Months: ',num_months)

#super complicatd code copied off website lol- changes currecy format
print('Total: ','${:,d}'.format(sum))

text_file.write('Total: ')
text_file.write(str('${:,d}'.format(sum)))
text_file.write("\n")

for n in range(0,num_months-1):
        change_val.append(int(profit_loss[n+1])-int(profit_loss[n]))

num_change = len(change_val)

sum = 0

for n in range(0,num_change):
        sum = sum + int(change_val[n])

avg_change = sum/num_change

print('Average Change: ','${:,.2f}'.format(avg_change))

text_file.write('Average Change: ')
text_file.write(str('${:,.2f}'.format(avg_change)))
text_file.write("\n")


most = max(change_val)

max_index = change_val.index(max(change_val))

least = min(change_val)

least_index = change_val.index(min(change_val))

print('Greatest Increase in Profits: ', month[max_index+1],'(','${:,d}'.format(most),')')

text_file.write('Greatest Increase in Profits: ')
text_file.write(month[max_index+1])
text_file.write('(')
text_file.write('${:,d}'.format(most))
text_file.write(')')
text_file.write("\n")
        
print('Greatest Decrease in Profits: ', month[least_index+1],'(','${:,d}'.format(least),')')

text_file.write('Greatest Decrease in Profits: ')
text_file.write(month[least_index+1])
text_file.write('(')
text_file.write('${:,d}'.format(least))
text_file.write(')')

text_file.close()