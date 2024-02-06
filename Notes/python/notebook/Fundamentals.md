# **1. Syntax and Basics:**

- ## **Indentation:** 
	- **HOTKEY TIP**: Use tab to indent deeper and shift + tab to undo or fix whitespace.
	- Unlike many languages, Python uses indentation to define code blocks instead of braces. Consistent indentation (usually 4 spaces) is crucial for program flow.
	- consistency is key.
	- whitespace matters. Random tabs and spaces can lead to errors and bugs.
	- If you want to end a code block, then reduce the indent level
	- [PEP-8 Style Guide](https://peps.python.org/pep-0008/)
	- Block structure: 
```
	if condition:
		# indent block
		do_something()
	else:
		# another indent block
		do_something_else()

	def my_function(): 
		print("Inside the function") 
	# Outside the function
```
		
- #### **Variables and Data Types:** 
	- ##### Variables - 
		- ##### (local and global): 
		- names are case sensitive
		- names must start as a letter or a underscore character
		- cannot start with a number
		- names can only contain letters, numbers, underscores and hyphens
		- names can never be keywords from the python language
		- Names with multiple words use Camel Case, Pascal Case, Snake Case
		- you can assign multiple variables with values in the same line
		- you can assign one value to many variables
		- ##### **Unpacking a Collection**: 
			- you can extract values from a list, tuple or dictionary to variables. 
		```
		ex: fruits = ["apple", "banana", "cherry"]   |    x, y, z = fruits
		```
		- ##### **Global Variables**: 
			- variables created outside functions are global, functions created inside functions are local and stay inside functions. You can make local variables global by first tagging it with **Global** . `ex: global x`
		- ##### **Local Variables**: 
			- these are variables created and stay inside functions and have no effect on global variables.
	- ##### **integers** - 
		- any whole numbers, either positive or negative.
		- integers support basic math operations: `(+, -, /, *)`
		- you can use `(//)` for division and this will result in the result being rounded down
		- `(%)` the modulo operator gives the remainder of the division of two numbers, if any.
		- **Exponents**: You can raise a number to a power using `(**)`
		```
		ex: simple_Exponents = 2 ** 3
		```
		- **Type Conversion**: convert other values to int -
		```
		str_to_int = int("string")
		float_to_int = int(3.14)
		```
		- **Importing Advanced math**:
		```
		import math
		result_sqrt = math.sqrt(16)
		```
		
	- ##### floats -
		- floats have many of the same rules of integers with a few differences mostly due to precision issues based on how they are represented.
	- ##### **strings (str)** - 
		- strings can be identified by single or double quotes. can also make multi-line string with three either double or single quotes
			`my_string = "Hello World"`
			`my_string = 'Hello World'`
		- Strings are immutable, meaning you cannot modify them once they are created. Operations on strings create new strings.
			`original_string = "Hello" `
			`modified_string = original_string + ", Python!"`
		- Strings are indexed from left to right starting at 0.
			`first_char = my_string[0]`
		- **slicing**: 
			- you can slice string with `[start:end] ` to specify start and end positions. Leaving them blank will start at beginning or end respectively. You can use negative values to start from the end. `ex:[-1:-3]`
			`substring = my_string[7:13]`
		- **Concatenation**:
		```
		greeting = "Hello" 
		name = "Chris" 
		full_greeting = greeting + ", " + name + "!" 
		```
		- **escape characters**:
			- Strings can include escape characters to represent special characters, like newline (`\n`) or tab (`\t`).
			- `multiline_string = "This is a line.\nThis is a new line."`
			- `multiline_string = """ This is a multiline string in Python. """`
		- **String methods**:
		```
		len(): Returns the length of the string.
		upper(): Converts the string to uppercase.
		lower(): Converts the string to lowercase.
		strip(): Removes leading and trailing whitespaces.
		replace(): Replaces a substring with another.
		find(): Returns the index of the first occurrence of a substring.
		count(): Counts the occurrences of a substring.
		split(): Split a string into a list where each word is a list item.
		startswith(): Checks if a string starts with a specified prefix.
		endswith(): Checks if a string ends with a specified suffix.
		capitalize(): Capitalizes the first character of a string.
		```
		- **Formatting strings**:
			- this allows you to inject variables and other code into strings
			```
			name = "Chris" 
			age = 28 
			formatted_string = f"My name is {name} and I am {age} years old."
			
			price = 19.99 
			quantity = 3 
			total = f"Total cost: {price * quantity:.2f}"
			```
	- **booleans** -
		- Booleans are truth evaluations and are two values: `true` and `false`
		- boolean keywords: `and` `or` and `not` 
		- false vales are `false` , `0` , `none` , and empty containers (`[]`, `{}`, `""` )
		- all other values are true
		```
		True and True # this is true
		False and False # this is false
		True and False # this is false
		False and True # this is false
		# AND only evaluates to true if both sides are true
		
		True or True # this is true
		False or False # this is false
		True or False # this is true
		False or True # this is true
		# OR only evaluates to false if both sides are false
		
		not true # this is false 
		not false # this is true
		# NOT results in reversing the result  
		```
		- Identity:
		- `is`, and `is not` are used to compare two objects in memory. used with `id()` this will allow the comparison to check the value.
		```
		x = [1, 2, 3]
		y = [1, 2, 3]
		
		print(x is y) # this is false
		print(x == y) # this is true
		```
		- `in` and `not in` are used to check if something is the member of a sequence (string, list, tuple)
		```
		 numbers = [1, 2, 3, 4, 5]
		 is_present = 3 in numbers # this is true
		```
		- short circuit:
			- bool expressions are evaluated per operand, the second part will not evaluate if the first resolves the comparison
			- `result = True or some_function()`
		- Comparison Chaining:
			- `x = 10`
			- `in_range = 5 < x < 15 # this is true`
		- Boolean Functions:
			- functions can return boolean values which can be used further
			```
			def is_positive(number): 
				return number > 0 
			
			result = is_positive(5) # result is True
			```
	- **NaN** -
		- NaN is a special value representing an undefined or unrepresentative result, typically arising from mathematical operations like division by zero or operations involving infinity.
		- NaN often occurs in numerical computations, especially when dealing with:
			- Division by zero.
			- Operations involving infinity.
			- Invalid mathematical operations.
		- math with NaN results in NaN
		- comparisons with NaN result in false
		- working with NaN is important in working with datasets and analysis and are represented as missing or unidentified values
	- None -
		- represents the absence of a value or undefined state
		- `result = none # no value`
		- functions that do not return a value explicitly return `none`
		- `None` is commonly used as a default value for function parameters when the absence of a specific argument value is significant.
		```
		 def greet(name=None): 
			 if name is None: 
				 name = "Guest" 
			 print(f"Hello, {name}!") 
			 
		 greet() # Hello, Guest! 
		 greet("John") # Hello, John!
		```
	- range -
		- the `range` function is used to generate a sequence of numbers most often used in loops. 
		- `range` takes up to 3 arguments:
			- `range(stop)` # when there is only one parameter, the range starts at 0 and stops at the number before the final number.
			- `range(start, stop)` the first value is where the range starts and then stops at the number before the second.
			- `range(start, stop, step)` the last option is how much the range increments by.
			```
			range_1 = range(5) # [0, 1, 2, 3, 4]
			range_2 = range(2, 8) # [2, 3, 4, 5, 6, 7]
			range_3 = range(1, 10, 2) # [1, 3, 5, 7, 9]
			```
			- range looping:
			```
			for i in range(3):
				print(i)
			# Output: 0
			#         1
			#         2
			
			```
- #### **Operators:** 
	- Master basic arithmetic, logical, comparison, and assignment operators to perform calculations and comparisons within your code.
		- comparison operators:
		```
		# Equality 
		is_equal = 5 == 3 + 2 # is_equal is True 
		
		# Inequality 
		not_equal = 10 != 5 # not_equal is True 
		
		# Greater than 
		greater_than = 8 > 5 # greater_than is True
		 
		# Less than or equal to 
		less_than_or_equal = 10 <= 10 # less_than_or_equal is True
		```
		- Ternary Operator:
		- Ellipsis (...) Operator:
		- Matrix Multiplication Operator:
	- **complex type**:
	- **binary**:
- #### **Input and Output (I/O):** 
	- Get comfortable with functions like `print()` for output and `input()` for user input.
	- `print(x) - normally used to print text or for debugging`
	- `input("please write something")`
- #### **Comments**: 
	- Comments start with a #, and Python will render the rest of the line as a comment.
	- `# this is a comment`
	- `""" this can also be a comment """`

# **2. Control Flow:**

- **Conditionals:** Use `if`, `else`, and `elif` statements to make decisions based on conditions and execute different code blocks accordingly.
- **Loops:** Employ `for` loops to iterate over sequences of elements and `while` loops for repeated execution based on a condition being true.
- **Functions:** Define functions to group related code blocks, increase modularity, and avoid repetition. Learn about arguments, return values, and local variables.
	- **casting**: 
		-converting the value of one type into the value of another
		- int() -
		- float() -
		- str() -
	- **internal functions**: 
		- random(), randrange(low, high) -

# **3. Data Structures:**

- **Lists:** Master creating and manipulating lists, mutable sequences of elements enclosed in square brackets. Understand indexing, slicing, and common list methods.
- **Tuples:** Explore immutable sequences similar to lists but defined with parentheses. Learn about their unique properties and use cases.
- **Dictionaries:** Key-value pairs enclosed in curly braces, dictionaries are perfect for storing and accessing data by unique keys. Understand accessing, updating, and iterating through dictionaries.
- **sets**:

# **4. Object-Oriented Programming (OOP):**

- **Classes and Objects:** Learn how Python utilizes classes as blueprints for creating objects with specific attributes and methods.
- **Inheritance:** Understand how to extend existing classes with new functionalities through inheritance, promoting code reuse and efficiency.
- **Encapsulation and Abstraction:** Grasp the concepts of data hiding and exposing essential functionalities through methods, enhancing code organization and security.

# **5. Error Handling and Debugging:**

- **Exceptions:** Learn how to anticipate and handle potential errors during program execution using `try`, `except`, and `finally` blocks.
- **Debugging Techniques:** Understand basic debugging practices like printing intermediate values, using breakpoints, and analyzing error messages.