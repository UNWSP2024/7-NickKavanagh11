# Program #3: US_Population
def main():

    data = []

    num_entries = int(input("How many records will you enter? "))

    for i in range(num_entries):

        year = int(input("Enter year: "))
        state = input("Enter state name: ")
        population = int(input("Enter population: "))

        data.append([year, state, population])

    search_year = int(input("\nEnter a year to calculate total population: "))

    total_population = 0

    for record in data:
        if record[0] == search_year:
            total_population += record[2]

    print(f"\nTotal population for {search_year}: {total_population}")

main()

"""
Sample Output:

How many records will you enter? 3
Enter year: 2010
Enter state name: Maine
Enter population: 1987435

Enter year: 2010
Enter state name: Minnesota
Enter population: 6873202

Enter year: 2011
Enter state name: Iowa
Enter population: 3421988

Enter a year to calculate total population: 2010

Total population for 2010: 8860637
"""
