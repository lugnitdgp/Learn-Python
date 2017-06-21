# A while-loop will keep executing the code block under it as long as a boolean expression is True.
# If we write a line and end it with a colon then that tells Python to start a new block of code. 
# Then we indent and that is the new  code. 
# This is all about structuring your programs so that Python knows what you mean.
# If you do not get that idea then go back and do some more work with if-statements, functions, and the for-loop until you get it.

# SAMPLE CODE

i = 0
numbers = []
while i < 6:
  print "At the top i is %d" % i
  numbers.append(i)
  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i
  print "The numbers: "
for num in numbers:
  print num
