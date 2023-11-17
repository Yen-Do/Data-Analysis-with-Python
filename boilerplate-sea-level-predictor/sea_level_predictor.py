import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level Data', marker='o')

    # Calculate the line of best fit for the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a line of best fit that extends to the year 2050
    year_range = range(1880, 2051)
    sea_level_predictions = [slope * year + intercept for year in year_range]
    plt.plot(year_range, sea_level_predictions, label='Line of Best Fit (1880-2050)', color='red')

    # Calculate the line of best fit for the data from year 2000 onwards
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    # Create a line of best fit that extends to the year 2050 for recent data
    recent_year_range = range(2000, 2051)
    recent_sea_level_predictions = [slope_recent * year + intercept_recent for year in recent_year_range]
    plt.plot(recent_year_range, recent_sea_level_predictions, label='Line of Best Fit (2000-2050)', color='green')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
