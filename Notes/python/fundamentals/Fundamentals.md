# **1. Syntax and Basics:**

- ## **Indentation:** 
	- Unlike many languages, Python uses indentation to define code blocks instead of braces. Consistent indentation (usually 4 spaces) is crucial for program flow.
- #### **Variables and Data Types:** 
	- integers -
	- floats -
	- strings (str) - 
		- strings can be identified by single or double quotes. can also make multi-line string with three either double or single quotes
		- **slicing**: you can slice string with [start:end] to specify start and end positions. Leaving them blank will start at beginning or end respectively. You can use negative values to start from the end. ex:[-1:-3]
	- boo-leans -
	- NaN -
	- range -
	- Variables - 
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
			- you can extract values from a list, tuple or dictionary to variables. ex: fruits = ["apple", "banana", "cherry"]   |    x, y, z = fruits
		- ##### **Global Variables**: 
			- variables created outside functions are global, functions created inside functions are local and stay inside functions. You can make local variables global by first tagging it with **Global**
		- ##### **Local Variables**: 
			- these are variables created and stay inside functions and have no effect on global variables.
- #### **Operators:** 
	- Master basic arithmetic, logical, comparison, and assignment operators to perform calculations and comparisons within your code.
- #### **Input and Output (I/O):** 
	- Get comfortable with functions like `print()` for output and `input()` for user input.
	- print(x) - normally used to print text or for debugging
	- input("please write something")
- #### **Comments**: 
	- Comments start with a #, and Python will render the rest of the line as a comment.
	- # this is a comment
	- """ this can also be a comment """

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
		- len() -
		- **String functions**:
			- upper() 
			- lower()
			- strip()
			- replace()
			- split()

# **3. Data Structures:**

- **Lists:** Master creating and manipulating lists, mutable sequences of elements enclosed in square brackets. Understand indexing, slicing, and common list methods.
- **Tuples:** Explore immutable sequences similar to lists but defined with parentheses. Learn about their unique properties and use cases.
- **Dictionaries:** Key-value pairs enclosed in curly braces, dictionaries are perfect for storing and accessing data by unique keys. Understand accessing, updating, and iterating through dictionaries.

# **4. Object-Oriented Programming (OOP):**

- **Classes and Objects:** Learn how Python utilizes classes as blueprints for creating objects with specific attributes and methods.
- **Inheritance:** Understand how to extend existing classes with new functionalities through inheritance, promoting code reuse and efficiency.
- **Encapsulation and Abstraction:** Grasp the concepts of data hiding and exposing essential functionalities through methods, enhancing code organization and security.

# **5. Error Handling and Debugging:**

- **Exceptions:** Learn how to anticipate and handle potential errors during program execution using `try`, `except`, and `finally` blocks.
- **Debugging Techniques:** Understand basic debugging practices like printing intermediate values, using breakpoints, and analyzing error messages.