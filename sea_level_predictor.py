import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(18,10))
    plt.scatter(df['Year'].values , df['CSIRO Adjusted Sea Level'].values, s=10, c='b', alpha=0.5)

    # Create first line of best fit
    regress_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(df['Year'].values, regress_all.intercept + regress_all.slope * df['Year'], label='Fit all', c='r')

    # Create second line of best fit
    df_new = df[(df['Year'] >= 2000) & (df['Year'] <= df['Year'].max())]
    regress_new = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    sea_level_2050_new = regress_new.intercept + regress_new.slope * 2050
    ax.plot(df_new['Year'].values, regress_new.intercept + regress_new.slope * df_new['Year'], label='Fit since 2000', c='g')

    # Add labels and title
    ax.set_xlabel('Year', fontsize=20)
    ax.set_ylabel('CSIRO Adjusted Sea Level (inches)', fontsize=20)
    ax.set_title('Sea Level Rise', fontsize=24)
    ax.legend(fontsize=16)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()