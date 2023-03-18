import random

# Define constants
LIST_SIZE = 10
MIN_NUMBER = 1
MAX_NUMBER = 100

# Generate a list of unique random numbers
numbers = set()
while len(numbers) < LIST_SIZE:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    numbers.add(number)

# Calculate the average of the numbers
total = sum(numbers)
average = total / len(numbers)

# Print the list and the average
print(f"List of unique random numbers: {numbers}")
print(f"Average of the numbers: {average}")
