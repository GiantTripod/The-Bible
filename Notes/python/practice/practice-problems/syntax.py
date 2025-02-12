'''**1. Hello World:** (Very Easy) Write a program that prints "Hello, World!" to the console.
'''
# message = input('What would you like to say? ')
# print(message)


'''**2. Number Addition:** (Easy) Write a program that takes two numbers as input and prints their sum.'''

# number1 = input('choose a number: ')
# number2 = input('choose a number: ')

# print(int(number1) + int(number2))


'''**3. Odd or Even:** (Easy) Write a program that takes a number as input and prints "Even" if it is even, "Odd" if it is odd, and "Neither" if it is zero.'''

# evenOrOdd = int(input('what number would you like to check? '))

# if evenOrOdd % 2 == 0:
#     print('even')
# else:
#     print('odd')


'''**4. Minimum of Three:** (Easy) Write a program that takes three numbers as input and prints the smallest number.'''

# ```
# a = int(input('Pick a number '))
# b = int(input('Pick a second number '))
# c = int(input('Pick a third number '))

# def smallestNumber(a, b, c):
#     if a < b and a < c:
#         print(a, 'a is smallest')
#     elif b < a and b < c: 
#         print(b, 'b is smallest')
#     else:
#         print(c, 'c is smallest')

# smallestNumber(a, b, c)
# ```

# **5. Reverse a String:** (Medium) Write a program that takes a string as input and prints the reversed string.

# ```


# ```

# **6. Palindrome Checker:** (Medium) Write a program that takes a string as input and checks if it is a palindrome (reads the same backward and forward).

# ```
	
# ```

# **7. Find the Factorial:** (Medium) Write a program that takes a number as input and calculates its factorial.

# ```
	
# ```

'''8. Fibonacci Sequence:** (Medium) Write a program that generates the first 10 numbers of the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, 34, 55).'''


# a = 0
# b = 1

# for i in range(1, 12):
#     print(a)
#     total = a + b
#     a = b
#     b = total



# **9. List Statistics:** (Challenging) Write a program that takes a list of numbers as input and calculates the minimum, maximum, average, and standard deviation.

# ```
	
# ```

# **10. Guessing Game:** (Challenging) Write a program that generates a random number between 1 and 100, and the user has to guess it within 5 tries. Give the user hints like "higher" or "lower" after each guess.

# ```
	
# ```

# **Bonus:**

# - Implement these problems using different functions and loops.
# - Add error handling to check for invalid input.
# - Make the programs more interactive with user prompts and menus.

# **1. Guessing Game (Very Easy):** Write a program that generates a random number between 1 and 100. Let the user guess the number within 5 attempts. Use `if` statements for feedback and print a congratulatory message if guessed correctly.

# ```
	
# ```

# **2. Area & Perimeter Calculator (Easy):** Write a program that takes the length and width of a rectangle as input and calculates its area and perimeter. Use basic operators and print the results.

# ```
	
# ```

# **3. Odd or Even? (Easy):** Write a function that takes a number as input and returns True if it's even and False if it's odd. Use the modulo operator (`%`) for checking evenness.

# ```
	
# ```

# **4. List Sorter (Medium):** Write a program that takes a list of numbers as input and sorts them in ascending order. Use a loop and conditional statements to achieve this. You can explore different sorting algorithms later.

# ```
	
# ```

# **5. Vowel Counter (Medium):** Write a function that takes a string as input and returns the number of vowels it contains. Use a loop and `in` operator to check for vowels.

# ```
	
# ```

# **6. Password Validator (Medium):** Write a program that asks the user for a password and checks if it's valid. The password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit. Use appropriate conditions and string methods.

# ```
	
# ```

# **7. Sentence Analyzer (Hard):** Write a program that takes a sentence as input and analyzes it. Find the number of words, the average word length, and the most frequent letter. Use string methods and loops for parsing and counting.

# ```
	
# ```

'''8. Fibonacci Sequence (Hard):** Write a function that takes a number `n` as input and generates the first `n` terms of the Fibonacci sequence. Use recursion or loop with memoization to achieve this.'''

# ```
# a = 0
# b = 1
# n = input('PICK A NUMBER: ')
# for n in range(1, int(n)):
#     print(a)
#     total = a + b
#     a = b
#     b = total

# ```

# **9. Tic-Tac-Toe Game (Challenging):** Write a program that implements a basic Tic-Tac-Toe game with two human players. Use a multidimensional list to represent the board and employ turn-based logic with user input handling.

# ```
	
# ```

# **10. Hangman Game (Challenging):** Write a program that implements the classic Hangman game. Let the user guess letters in a secret word while avoiding exceeding a predetermined number of wrong guesses. Use string manipulation and conditional logic to manage the gameplay.

# ```
	
# ```


# ### Easy:

# 5. Write a program to calculate the area of a rectangle. Take the length and width as input from the user.
# 6. Create a function that takes two numbers as parameters and returns their sum.
# 7. Use a loop to print the numbers from 1 to 5.
# 8. Define a dictionary with at least three key-value pairs representing information about your dog.

# ### Medium:

# 9. Write a program to check if a number is even or odd.
# 10. Create a function that checks if a given word is a palindrome (reads the same backward as forward).
# 11. Implement a simple calculator that can add, subtract, multiply, or divide two numbers based on user input.
# 12. Write a program that finds the largest number in a list.

# ### Hard:

# 13. Create a class called `Person` with attributes for name and age. Create an object of this class and print its details.
# 14. Write a program to find all prime numbers between 1 and 50.
# 15. Implement a guessing game where the computer randomly selects a number, and the user has to guess it.
# 16. Create a function that calculates the factorial of a given number.

# ### Very Hard:

# 17. Implement a text-based adventure game using functions and conditional statements.
# 18. Write a program to sort a list of numbers in ascending order without using built-in functions.
# 19. Create a program that simulates a basic file system with commands like create file, delete file, create directory, etc.
# 20. Build a simple web scraper in Python that extracts information from a website.


'''Consider a scenario where you're given a list of integers, and your task is to write a Python script that finds the sum of all the even numbers in the list.'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = 0

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers = number + even_numbers
    
# print(even_numbers)



'''Create a Python script that prints a simple number pyramid pattern. The pattern for a pyramid with 5 levels should look like this:

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 '''


# levels = int(input('how big is your pyramid? '))

# for level in range(1, levels + 1):
#     for _ in range(level):
#         print(level, end=' ')
#     print()



'''Write a script that checks numbers from 1 to 50 and prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both 3 and 5, and the number itself for all other cases.

This problem, often called "FizzBuzz", is a classic programming challenge that tests your understanding of both loops and conditionals. Here's how you can approach it:

Use a loop to iterate through numbers 1 to 50.
For each number, you'll need a series of if statements (or one combined statement using elif) to check the conditions:
If the number is a multiple of both 3 and 5 (you can use the modulo operator % to check for no remainder).
If the number is only a multiple of 3.
If the number is only a multiple of 5.
If none of the above conditions are true, just print the number.
Print the appropriate response based on these conditions.'''


# fizzy_Numbers = int(input('how many bubbles do you want? '))

# for fizz in range(1, fizzy_Numbers + 1):
#     if fizz % 5 == 0 and fizz % 3 == 0:
#         print('fizzbuzz')
#     elif fizz % 5 == 0:
#         print("buzz")
#     elif fizz % 3 == 0:
#         print("fizz")
#     else:
#         print(fizz)