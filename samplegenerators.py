# Generators hold values that are fetched lazily. 
# Meaning that the entire collection isn't stored
# in memory all at once, but rather retrieved when
# needed.

# This is best used when dealing with a large 
# collection of items. Such as rows returned from 
# a database call or looping over a large csv. 

# Generators are intelligent enough to handle these
# large collections without running out of memory. 
# They dispose of variables in memory that are no
# longer used and do not worry about variables
# that are not yet needed.

# Here's the syntax for a generator. It's just a
# function! Take note of the yield keyword. yield
# basically means 'return', but lets Python know
# we'll be coming back for more. 
def color_generator():
    yield 'blue'
    yield 'orange'
    yield 'yellow'
    yield 'purple'

# One way to use generators is by calling `next()`
# on it's instance
g = color_generator()  # create the instance
next(g)  # 'blue'
next(g)  # 'orange'
next(g)  # 'yellow'
next(g)  # 'purple'

# However, once a generator is exhausted, it will
# not start back at the beginning. 
next(g)  # Raises StopIteration error.

# They're also iterables. No StopIteration errors
# are thrown with this method. 
for color in color_generator():
    print(color)

# 'blue'
# 'orange'
# 'yellow'
# 'purple'

