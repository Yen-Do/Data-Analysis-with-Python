import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting the index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Create a copy of the DataFrame
    df_line = df.copy()

    # Create line plot
    fig, ax = plt.subplots(figsize=(14, 6))
    plt.plot(df_line.index, df_line['value'], color='r', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    # Extract year and month from the date column
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    
    # Group by year and month, calculate the mean, and unstack the data
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Create bar plot
    fig, ax = plt.subplots(figsize=(14, 6))
    df_bar.plot(kind='bar', ax=ax)
    plt.title('Average Page Views per Month (2016-2019)')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=45)
    
    # Set the legend labels to months of the year
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    ax.legend(title='Months', labels=month_order)
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Create box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    sns.boxplot(data=df_box, x='month', y='value', order=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ], ax=axes[1])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

