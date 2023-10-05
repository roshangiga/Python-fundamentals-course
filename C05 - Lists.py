# -------------------------------------------------------------------------------------------------------
# Question 1
# -------------------------------------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 Ask the user for input and append
user_input = input("Please enter a value: ")
user_list.append(user_input)

# 2. Remove odd numbers from list and print it.
# for i in range(len(nums)-1):
#   if (i % 2 == 1):
#     nums.remove(i)
#   
# print(nums)

# 3. Print this list by reversing it using slicing.
print(nums[-1::-1])

# 4. Change the last element to 0.
nums[-1] = 0
print(nums)

# -------------------------------------------------------------------------------------------------------
# Question 2
# -------------------------------------------------------------------------------------------------------

even_numbers = []

for x in range(4, 31):
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)
