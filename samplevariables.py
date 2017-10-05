#this will teach about all of the various variable types in python
#first up, we have the numbers variable type, which covers everything from simple numbers to integers and long numbers
int_type = 5 #int is basically for regular numbers. no decimals, etc.
print int_type
float_type = 1.253 #float will recognize as many decimals as used in the dataset
print float_type
long_type = 51019272639284L #long is a less common type, but is used for longer numbers, hence the name
print long_type
complex_type = 12.134j #complex is another less common type. it is used for more mathematical and scientific programs
print complex_type
#
#
#
#next up is the string variable. strings consist of words or 
#anything that should be displayed or stored in plaintext format
string_type = 'abcdefghijklmnopqrstuvwxyz'
string_type2 = "We can use either a single apostrophe or quotation marks to store strings."
string_type3 = "We use quotations for ease when using apostrophes, like in contractions such as can't and won't"
print string_type
print string_type2
print string_type3
#
#
#
# next up is lists. lists are very useful! they can be edited in a number of different ways.
list_a = ['abc','def','ghi','jkl','mno','pqr','stu','vwx','yz']#lists can store any variable type(even other lists!), but strings are used here just as an example
print list_a
del list_a[0]#here we deleted the first instance of 'abc'
list_a.append('abc')#and then added it to the end of the list
print list_a
#
#
#
# similar to lists is a variable called tuples. tuples are essentially lists, but they cannot be edited as lists can. think of them as "read only"
tuple_a = ('abc','def')
print tuple_a
#
#
#
# dictionary types are basically superlists. they can store an item (called a key) like a list, but also has a corresponding value.
# if you wanted to store a list of grocery store departments and their phone extensions, you could do so in a dictionary!
dict_a = {'deli': 123, 'produce': 456, 'non-perishables': 789, 'floral': 000,}
print dict_a #this will print all of the keys and their values
