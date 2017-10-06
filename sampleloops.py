
arr=[1,2,3] #this is a simplae list wich can consider as an array
arrstr=["ashu" , "himu" , "piyu"]
for num in arr: #take the each element in the arr list to the num variable
    print "numbers are %d" %num
for name in arrstr: #take the each element in the arrstr list to the num variable
    print "names are %s" %name
arrinput=[] #take an empty list
for i in range(0,4): #loop in a selected range (i=0,1,2,3)
    print "enter element number %d" %i
    number = raw_input("> ")
    arrinput.append(number) #save the each input value in to the empty list named arrinput
for inp in arrinput: #take the each element in the arrinput list to the num variable
    print "elements are %r" %inp   
