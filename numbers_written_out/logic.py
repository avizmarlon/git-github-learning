from ext_nums_data import *

# todo.*add hyphen in the extensive form of some numbers
# todo.* make it scalable to even bigger numbers
# maybe wrap all the code into a function to be used by other scripts

# take the input, check if its a valid integer
# also eliminates redundant zeroes in case of something like 01 or 00001
number = input("Type the number to be written out: ")
try:
    number = int(number)
except ValueError:
    print("Your input was not an integer!")
    exit()

# converts back to str to be iterable
number = str(number)

# breaks the number into "smaller pieces" to easily work with the dict (e.g.: 435 becomes 400+30+5)
simple_numbers = []
c = 0
for character in number:
    current_iteration_number = number[c:]
    simple_number = character + ('0' * (len(current_iteration_number) - 1))
    c += 1
    simple_numbers.append(int(simple_number))

# print the extensive form, number by number (iterated through the list of decimal numbers)
for simple_number in simple_numbers:
    print(ext_nums[simple_number], end=' ')




# testing string format for output of 3-characters number (NOT FINISHED)
# '{num1}{num2}{num3}'.format(num1=ext_nums[simple_numbers[0]],
#                             num2=ext_nums[simple_numbers[1]],
#                             num3=ext_nums[simple_numbers[2]])
