# -------------------------------------------------------------------------------------------------------
# Question 1
# -------------------------------------------------------------------------------------------------------

# Ask for name
NAME = input('Enter your name: ')

# Print
print("Hello, " + NAME)

# -------------------------------------------------------------------------------------------------------
# Question 2
# -------------------------------------------------------------------------------------------------------

# Ask for age
age = input('Enter your age: ')

# Calculate months. Remember to convert age to int
age = int(age) * 12

# Print age by how many months
print(str(age) + " months")

# -------------------------------------------------------------------------------------------------------
# Question 3
# -------------------------------------------------------------------------------------------------------

# Ask for title
title = input('Enter your title: ')

# Ask for director
director = input('Enter your director: ')

# Ask for release year
year = input('Enter your release year: ')

# Print
print(title + " ("+ year +"), directed by "+ director)
