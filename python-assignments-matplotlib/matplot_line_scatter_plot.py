import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
#Population of the world in billions
pop = [2.519, 3.692, 5.263, 6.972]

#Creates a line plot
plt.plot(year, pop)
plt.show()

#Creates a scatterplot
plt.scatter(year, pop)
plt.show()