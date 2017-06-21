arr=[1,2,3]
arrstr=["ashu" , "himu" , "piyu"]
for num in arr:
    print "numbers are %d" %num
for name in arrstr:
    print "names are %s" %name
arrinput=[]
for i in range(0,4):
    print "enter element number %d" %i
    number = raw_input("> ")
    arrinput.append(number)
for inp in arrinput:
    print "elements are %r" %inp   
