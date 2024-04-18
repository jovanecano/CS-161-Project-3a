# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04-13-2024
# Description: This program asks the user to enter the number of integers they'd like to list, asks the user to list them, and then prints out the min/max values

num_ints = int(input("How many integers would you like to enter?\n")) # asking the user to input the number of values theyd like to enter

min_value = 0 # initializing the min value variable and assigning 0 to it
max_value = 0 # initializing the max value variable and assigning 0 to it

print(f"Please enter {num_ints} integers.")
for num in range(1, num_ints + 1): # looping through the range 1 to num_ints (including last number)
    current_number = int(input())
    if num == 1: # if its the first number entered, it assigns it as the min and max value
        min_value = current_number
        max_value = current_number
    else: # checks if the following numbers are less than / greater than current number
        if current_number < min_value:
            min_value = current_number
        if current_number > max_value:
            max_value = current_number

# displaying the min and max values
print(f"min: {min_value}")
print(f"max: {max_value}")
