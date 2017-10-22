# coding: utf-8

# prints an empty space since comments are ignored
print #"Hello World!"

# prints the following strings and separate lines
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

# prints the boolean value of this mathematical comparison
print 3 + 2 < 5 - 7

# assigning numerical values to variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# performing mathematical operations on the variables above,
# and assigning the answers to new variables
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# the new variables are printed on separate lines
print "We need to put about", average_passengers_per_car, "in each car."
print "We have", passengers, "to carpool today."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "There are only", drivers, "drivers available."
print "There are", cars, "cars available." 

# In all these lines of code, one thing got lost in the process:
# the first line. When we code, most of the things are wrote in
# english, but sometimes we need those things in another language.
# Languages like Portuguese and Spanish have accents, special
# characters and some other stuff that, when we try to print, 
# its outputed wrong. To correct that, in the first line of the
# code, we simply add a comment, on the first line, with the sentence
# "coding: utf-8", as we can see on this file. Adding it, we can
# print sentences like:

print "Olá mundo!" # portuguese for "Hello World!"


