# import command line argument reader 'argv' from the 'sys' python module
from sys import argv

# takes the two arguments after the 'python' command,
# and assigns to the variables 'script' and 'user_name'
script, user_name = argv

# assigns the string with an arrow and space to the variable 'prompt'
prompt = '> '

# user_name, the second argument, and 'sampleimport.py' replace %s in the order listed
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

# replaces %s with the variable user_name and prints
print "Do you like me %s?" % user_name

# prints '> ' and allows user to input a value, assigns user input to the 'likes' variable
likes = raw_input(prompt)

# repeats the process above two more times
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)

# takes the last three user inputs in order and inserts into the last print statement, replacing %r
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
