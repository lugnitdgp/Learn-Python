# Hi! Welcome to this mini tutorial on using list comprehensions in Python!
# Check out samplelists.py if you need help with lists.

# Starting off with list comprehensions!
# Syntax used to make an ordinary list:
my_list = ["apple", "banana", "pear", "peach"]

# To concisely make a new list of elements, use a list comprehension:
list_comp = [num for num in range(10)]  # Notice how square brackets are
# used to create a list.
print list_comp

# List comprehension syntax can be understood as so:
#           [num for      num in       range(5)]
# Make a new num for each num in given range

# The first expression (before the "for" keyword) can be altered to satisfy a
# given condition over an iterable.
doubled_list_comp = [num * 2 for num in list_comp]
print doubled_list_comp

# Furthermore, "if" statements can be used in list comprehensions as well.
even_num_list_comp = [num for num in list_comp if num % 2 == 0]
print even_num_list_comp
