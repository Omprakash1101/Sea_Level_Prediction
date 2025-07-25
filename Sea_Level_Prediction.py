import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  df = pd.read_csv('epa-sea-level.csv')

  # Create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  plt.scatter(x, y)

  # Use the linregress function to get the slope and y-intercept of the line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(x, y)

  # Create a range of years from 1880 to 2050
  years = range(1880, 2051)

  # Plot the line of best fit
  plt.plot(years, intercept + slope * years, 'r', label='Linear Regression')

  # Plot a new line of best fit using data from year 2000 onwards and extend it to the year 2050
  x_since_2000 = df[df['Year'] >= 2000]['Year']
  y_since_2000 = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
  slope_since_2000, intercept_since_2000, r_value_since_2000, p_value_since_2000, std_err_since_2000 = linregress(
    x_since_2000, y_since_2000)
  years_since_2000 = range(2000, 2051)
  plt.plot(years_since_2000,
           intercept_since_2000 + slope_since_2000 * years_since_2000,
           'g',
           label='Linear Regression since 2000')

  # Set the x label, y label, and title of the plot
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Show the legend
  plt.legend()
  # Read data from file

  # Create scatter plot

  # Create first line of best fit

  # Create second line of best fit

  # Add labels and title

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
