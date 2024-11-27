import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import seaborn as sns
import pandas as pd
import numpy as np

def draw_plot():
# Read data from file
    data = pd.read_csv("epa-sea-level.csv")

# Create scatter plot
    sns.scatterplot(x = data.Year, y= data['CSIRO Adjusted Sea Level'])

# Create first line
    firstLine = linregress(data.Year, data['CSIRO Adjusted Sea Level'])
    x = np.arange(data['Year'].min(), 2051)
    y = (firstLine.slope)*(x) + firstLine.intercept
    plt.plot(x, y)

# Create second line
    data_2020 = data[data['Year'] >= 2000]
    secondLine = linregress(data_2020.Year, data_2020['CSIRO Adjusted Sea Level'])
    x = np.arange(2000, 2051)
    y = (secondLine.slope)*(x) + secondLine.intercept
    plt.plot(x, y)

# Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level.')
    
# Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()
    return plt.gca()

draw_plot()