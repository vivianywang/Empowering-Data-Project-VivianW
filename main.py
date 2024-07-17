# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

print("Here is a scatter plot representing the average amount of rainfall in Colombia (located in South America) and Senegal (located in Africa) between 1990 to 2015.")
input("\nPress enter to continue")
print("Colombia is the country with the most amount of rainfall and Senegal one with one of the least amount of rainfall. \nResearchers say that Colombia has so much rainfall due to its proximity to the equator while Senegal has a presence of the subtropical ridge with subsiding, hot, dry air masses.\n")
input("Press return to continue")
print("\nThe people of Colombia are probably ued to immense amounts of rainfall and their emotions and backstories aren't affected by it. ALthought this is true, there are probably people who moved there that are struggling to keep up with the rainy weather. Same goes for Senegal and the dryness of the country.\n")
input("Press return to continue")
print("\nAs we can see in the graph, the rainfall amounts in both countries are significantly different. But one thing is similar in both. There have been abnormal trends going on in the past decade. In Colombia, rainfall amounts have been steadily decreasing by significant amounts. In Senegal, thre has been sudden jumps of great amounts of rainfall then sudden decreasing in the past few years. \n \nCould this be related to global warming in any way?")

oneCountryBooleanList = lwd["country_name"] == "Senegal"
twoCountryBooleanList = lwd["country_name"] == "Colombia"
oneCountryData = lwd.loc[oneCountryBooleanList]
twoCountryData = lwd.loc[twoCountryBooleanList]

# create a scatter plot
plt.scatter(label="Senegal", x="year", y="pre_mean12", data = oneCountryData)
plt.scatter(label="Colombia", x="year", y="pre_mean12", data = twoCountryData)

# add a title to the plot
plt.title("Average Precipitation Per Month")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Precipitation (mm)")
plt.legend(loc = "upper left")
# show the plot
plt.show()
