# newline
print("The itsy bitsy spider\nclimbed up the waterspout.")
# Output
""" The itsy bitsy spider
climbed up the waterspout. """

# Escape
print('Joseph"s leash')
# Output
""" Joseph\"s leash """

# Multiple Arguments
print("The itsy bitsy spider", "climbed up", "the waterspout.")
# Output
""" The itsy bitsy spider climbed up the waterspout. """

# Positional arguments - the second argument will be outputted after the first
print("The itsy bitsy spider", "climbed up", "the waterspout.")
# Output
""" The itsy bitsy spider climbed up the waterspout. """

# Keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.")

""" In our example, we have made use of the end keyword argument, 
and set it to a string containing one space. """

# Output
""" My name is Python. Monty Python. """

print("My", "name", "is", "Monty", "Python.", sep="-")

# Output
""" My-name-is-Monty-Python. """


# Example
# Output: Programming***Essentials***in...Python

print("Programming","Essentials","in",sep="***", end="...")
print("Python")