# import command line argument reader 'argv' from the 'sys' python module
from sys import argv

# takes the four arguments after the 'python' command,
# and assigns to the variables 's', 'f', 'ss', and 't'
s,f,ss,t=argv

# prints the four arguments on separate lines with text
print "the script is" , s
print "var1 1 is" , f
print "var 2 is" , ss
print "var 3 is" , t
