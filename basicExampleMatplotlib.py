#Usage 'as plt' is a convention
import matplotlib.pyplot as plt

year = [2000, 2005, 2010]

population = [7.823, 7.965, 8.012]

#Create a plot graph with abscissas and ordenate	
plt.plot(population, year)

#add the values on abscissas and ordenate
plt.xlabel('Population')
plt.ylabel('Years')

#Setting a title to the graph
plt.title('Graphs Population x Years')

#showing the graph
plt.show()


