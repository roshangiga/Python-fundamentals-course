# -------------------------------------------------------------------------------------------------------
# Question 1 - Number guesser
# -------------------------------------------------------------------------------------------------------

import random

number_to_guess = random.randint(1, 100)
attempts = 10

# Enter rest of code
for i in range(attempts):
  
  user_guess = int(input("Enter guess " + str(i+1) + ": "))
  
  if (user_guess == number_to_guess):
  	print("Correct! You won!")
  	break

  elif (user_guess > number_to_guess):
  	print("Too high!")

  elif (user_guess < number_to_guess):
  	print("Too low!")

# -------------------------------------------------------------------------------------------------------
# Question 2 - Dot Product of Matrices
# -------------------------------------------------------------------------------------------------------


print("Enter the dimensions of the first matrix (rows, columns)")
m1_rows = input("Enter num of rows: ")
m1_cols = input("Enter num of columns: ")

# Prompt same for Matrix 2
m2_rows = input("Enter num of rows matrix 2: ")
m2_cols = input("Enter num of columns matrix 2: ")

# Enter rest of code

result = int(m1_cols) == int(m2_rows)

# Output
if result:
    print("A dot product can be calculated. The resulting matrix would have dimensions: " + str(result)) # Add resulting dimension
else:
    print("A dot product cannot be calculated with these dimensions.")


# -------------------------------------------------------------------------------------------------------
# Question 3 - Fibonacci
# -------------------------------------------------------------------------------------------------------

num = int(input("Enter the number of Fibonacci numbers to generate:"))

def fib(n):
  if (n == 0):
    return 0
    
  if (n == 1 or n == 2):
    return 1
    
  return fib(n-1) + fib(n-2)
  
print(fib(num))

# -------------------------------------------------------------------------------------------------------
# Question 4 - Palindrome
# -------------------------------------------------------------------------------------------------------

name = input("Enter name: ")

name_reversed = name[-1::-1]

if (name == name_reversed):
	print("Yes")
else:
	print("nope")


# -------------------------------------------------------------------------------------------------------
# Question 5 - Matrix Transpose
# -------------------------------------------------------------------------------------------------------

matrix = [
  	[1, 5],
  	[2, 0],
  	[7, 8],
]
  
for row, col in matrix:
  print(row),
  
print
  
for row, col in matrix:
  print(col),
