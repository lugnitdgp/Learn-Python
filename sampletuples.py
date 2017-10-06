# SAMPLE CODE TO ILLUSTRATE TUPLES IN PYTHON

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print "tuple: ", days

# a tuple is a collection
for day in days:
    print day

print day[0]

# we can get each element in a tuple
monday, tuesday, wednesday, thursday, friday, saturday, sunday = days
print monday, tuesday, wednesday, thursday, friday, saturday, sunday

# A tuple also can have differents types. Arrays, dicts even other tuples
tupleMix = (1,"happy", 3.1416, True, [1,2], {"lang": "English"}, (1,2))
print tupleMix

# we can concat tuples
a = (1,2,3)
b = (4,5,6)
c = a + b
print c

# or multiply a tuple
a = ("hi",) * 4 
print a

# :) learn more about tuples right here https://docs.python.org/3.1/tutorial/datastructures.html