# assigns numbers 1 through 3 to an array
arr=[1,2,3]

# assigns three names to an array
arrstr=["ashu" , "himu" , "piyu"]

# loops through each number from the number array, and prints the number
for num in arr:
    print "numbers are %d" %num

# loops through each name from the name array, and prints the name
for name in arrstr:
    print "names are %s" %name

# initializes an empty array
arrinput=[]

# asks the user for a input four times and pushes inputs into an array
for i in range(0,4):
    print "enter element number %d" %i
    number = raw_input("> ")
    arrinput.append(number)

# loops through the input array and prints each input
for inp in arrinput:
    print "elements are %r" %inp   
