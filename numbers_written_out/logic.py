from ext_nums_data import *

# take the input, check if its a valid integer
number = input("Type the number to be written out: ")
try:
    int(number)
except ValueError:
    print("Your input was not an integer!")
    exit()

# breaks the number into "smaller pieces" to easily work with the dict (e.g.: 435 becomes 400+30+5)
num_decimals = []
c = 0
for character in number:
    current_iteration_number = number[c:]
    decimal_number = character + ('0' * (len(current_iteration_number) - 1))
    c += 1
    num_decimals.append(int(decimal_number))

# print the extensive form, number by number (iterated through the list of decimal numbers)
for decimal_number in num_decimals:
    print(ext_nums[decimal_number], end=' ')




# testing string format for output (NOT FINISHED)
# '{num1}{num2}{num3}'.format(num1=ext_nums[num_decimals[0]],
#                             num2=ext_nums[num_decimals[1]],
#                             num3=ext_nums[num_decimals[2]])