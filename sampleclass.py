# SAMPLE CODE TO ILLUSTRATE CLASSES IN PYTHON



class TheThing(object): # Create the class Structure named 'TheThing'
  def __init__(self): #This step Creates the Initial data (__init__(self) method calls it self)
    self.number = 0 #This step creates a new attribute named 'number' and it's value is '0'
  def some_function(self): #some_function is a method named 'Some Function'
    print "I got called." #when calling to this method it prints 'I got called'
  def add_me_up(self, more): #another method with a prameter 'more'.
    self.number += more #calculate the addition of variables 'more' and 'number (in the initial)'
    return self.number #returns the number calculated
# two different things
a = TheThing() # 'a' and 'b' is a object of the class
b = TheThing()
a.some_function() # calling the methods inside the class individually
b.some_function()
print a.add_me_up(20) # the number '20' is assigned to the variable 'more' in the 'add_me_up' method in the class 
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)
print a.number #prints the calculated Number
print b.number
