# A while-loop will keep executing the code block under it as long as a boolean expression is True.
# If we write a line and end it with a colon then that tells Python to start a new block of code. 
# Then we indent and that is the new  code. 
# This is all about structuring your programs so that Python knows what you mean.
# If you do not get that idea then go back and do some more work with if-statements, functions, and the for-loop until you get it.

# SAMPLE CODE

# initialize the while iterator to 0
i = 0

# initialze empty numbers array
numbers = []

# keep running this while loop as long as 'i' is less than 6
while i < 6:

  # prints the value of i at the beginning of the loop
  print "At the top i is %d" % i

  # adds the number i to the number array
  numbers.append(i)

  # increase the number i by 1
  i = i + 1

  # prints the current numbers array
  print "Numbers now: ", numbers

  # prints the value of i at the end of the loop
  print "At the bottom i is %d" % i

# prints the numbers of the numbers array,
# every value of i during the loop before it exited (0 through 5)
# since the while loop exited when i reached 6
print "The numbers: "
for num in numbers:
  print num
