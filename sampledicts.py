# SAMPLE CODE TO UNDERSTAND THE CONCEPT OF DICTIONARIES IN PYTHON

#The pythond Dictionaries have two things, 
#1st one is the key and secon one is the value
#The function of the dictionary is when calling the key in dic. it returns the value in the key

#This is a Dictionary
cities = {'CA': 'San Francisco', 'MI': 'Detroit','FL': 'Jacksonville'} #Each key and value is separated by ':'
#Calling the key inside the dictionary and it returns the value belongs to the key
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#This is a function 'themap' is the dictionary and 'state' is the key
def find_city(themap, state):
  if state in themap: #if the 'state' is in the dictionary return the key's value
    return themap[state]
  else:
    return "Not found." #if the requested key is not in the dictionary it prints 'Not Found'
# ok pay attention!

cities['_find'] = find_city #Assign the function in to a variable 'cities['_find']'

while True: #This is a loop wich run until user press enter
  print "State? (ENTER to quit)", 
  state = raw_input("> ") # save user inputs into the 'state' variable
  if not state: break

# this line is the most important ever! study!
  
  city_found = cities['_find'](cities, state) #call the funtion written before
  print city_found #print the returned value
