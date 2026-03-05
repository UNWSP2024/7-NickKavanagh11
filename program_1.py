# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def main():

    months = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    rainfall = []

    for month in months:
        amount = float(input(f"Enter rainfall for {month}: "))
        rainfall.append(amount)

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12

    highest = max(rainfall)
    lowest = min(rainfall)

    highest_month = months[rainfall.index(highest)]
    lowest_month = months[rainfall.index(lowest)]

    print("\nRainfall Statistics")
    print("-------------------")
    print(f"Total rainfall: {total_rainfall}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Highest rainfall: {highest} in {highest_month}")
    print(f"Lowest rainfall: {lowest} in {lowest_month}")

main()

"""
Sample Output:

Enter rainfall for January: 3
Enter rainfall for February: 2
...
Enter rainfall for December: 4

Rainfall Statistics
-------------------
Total rainfall: 42
Average monthly rainfall: 3.50
Highest rainfall: 6 in June
Lowest rainfall: 1 in February
"""
