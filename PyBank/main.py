import csv,os

file = os.path.join('Resources','budget_data.csv')

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    row = next(csv_reader)

# Initializing the variables
    total_months = 0
    total_revenue = 0
    changes = []
    date_count = []
    greatest_increase = 0
    greatest_increase_month = 0
    greatest_decrease = 0
    greatest_decrease_month = 0

#Calculating total number of months and total revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csv_reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        #Calculate change from this month to previous months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])

        #calculate the greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #calculate the greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    #Calculating the average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    #Print all values
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: $" + greatest_increase_month, max(changes))
    print("Greatest Decrease in Profits: $" + greatest_decrease_month, min(changes))
