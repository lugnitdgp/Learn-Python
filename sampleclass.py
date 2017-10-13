# SAMPLE CODE TO ILLUSTRATE CLASSES IN PYTHON

# here we define a class
class TheThing(object):
  # this is a constructor
  def __init__(self):
    self.number = 0 # this is a attribute
  
  # here we define a method
  def some_function(self):
    print "I got called."

  # here we define a method and return a value
  def add_me_up(self, more):
    self.number += more # here 
    return self.number

# we have one instance
a = TheThing()

# here we have other instance
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number

# learn more about classes here https://docs.python.org/2/tutorial/classes.html