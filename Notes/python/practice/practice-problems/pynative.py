"""Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum."""



# def multiadd(x, y):
#     if x*y > 1000:
#         print(x*y)
#     else:
#         print(x+y)


"""Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number."""

# multiadd(int(input('enter number ')), int(input('enter another number ')))

# for x in range(int(input()), int(input())):
#     currentnumb = x
#     previousnumb = x - 1
#     if previousnumb < 0:
#         previousnumb = 0
#     sum = currentnumb + previousnumb
#     print(f'current number is: {currentnumb} Previous number is: {previousnumb} and the sum is: {sum}')


"""Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number."""

# string = input('longest word... ')

# for x in range(len(string)):
#     if x % 2 == 0:
#         print(string[x])
#     else:
#         pass

"""Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

    remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
    remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.

Note: n must be less than the length of the string."""

# word_slice = input('what word are we slicing? ')
# num_chars = int(input('how many letters are we slicing? '))

# def remove_chars(word_slice, num_chars):
#     sliced = word_slice[num_chars:]
#     print(sliced)

# remove_chars(word_slice, num_chars)


"""Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
"""

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def comp_num(list):
#     if list[0] == list[-1]:
#         print(True)
#     else:
#         print(False)

# comp_num(numbers_y)
# comp_num(numbers_x)
