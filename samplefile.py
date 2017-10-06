from sys import argv #import some system libraries
script , filename =argv 
txt=open(filename) #open the file
print "here is your file %r" %filename #print file name
print txt.read() #read the text inside the file
print "i'll also ask you to type it again"
fi=raw_input("> ") #take a input (file name)
tx=open(fi) #open the file named as user input
print tx.read() #read the file data and print it
