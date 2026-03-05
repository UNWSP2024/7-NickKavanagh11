# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def larger_than_n(num_list, n):
    for num in num_list:
        if num > n:
            print(num)


def main():

    numbers = []

    size = int(input("How many numbers would you like to enter? "))

    for i in range(size):
        value = float(input("Enter a number: "))
        numbers.append(value)

    n = float(input("Enter the comparison number (n): "))

    print(f"\nNumbers greater than {n}:")
    larger_than_n(numbers, n)


main()

"""
Sample Output:

How many numbers would you like to enter? 5
Enter a number: 4
Enter a number: 8
Enter a number: 2
Enter a number: 10
Enter a number: 5
Enter the comparison number (n): 5

Numbers greater than 5:
8
10
"""
