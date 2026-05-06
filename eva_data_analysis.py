import csv
import json
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def main(input_file, output_file, graph_file):
    print("--START--")

    # read data from JSON file
    eva_data = read_json_to_dataframe(input_file)

    # convert and export data to csv
    write_dataframe_to_csv(eva_data, output_file)

    eva_data.sort_values('date', inplace=True)

    # calculate eva durations in hours and the cumulative eva time 
    # and store them in the same dataframe.

    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a pandas dataframe.
    Cleans the data by removing any rows where the duration/date is missing.

    Args:
        input_file (file or string): File object or path to JSON file.

    Returns:
        eva_df (pd.Dataframe): cleaned up data in a pandas dataframe.
    """
    print(f"reading JSON file from {input_file.name}")
    df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    df['eva'] = df['eva'].astype(float)
    # remove rows which don't have duration or date entries
    df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return df

def write_dataframe_to_csv(df, output_file):
    """
    Writes pandas dataframe to csv file.

    Args:
        df (pandas.Dataframe): data to be written
        output_file (file or string): location to write data to
    """
    print(f"converting json to csv and writing to {output_file.name}")
    df.to_csv(output_file, index=False, encoding='utf-8')

def plot_cumulative_time_in_space(df, graph_file):
    """
    Plot the cumulative eva time against date

    Args:
        df (pandas.Dataframe): eva data
        graph_file (file or string): location to save figure to
    """
    # plot cumulative eva time against date
    print(f"plotting cumulative time in space {graph_file}")
    df = add_duration_hours(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/6  # there is an intentional bug on this line (should divide by 60 not 6)
    return duration_hours


def add_duration_hours(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(
        text_to_duration
    )
    return df_copy


if __name__ == "__main__":
    # Data source: https://data.nasa.gov/resource/eva.json (with modifications)
    input_file = open('./eva-data.json', 'r', encoding='ascii')
    output_file = open('./eva-data.csv', 'w', encoding='utf-8')
    graph_file = './cumulative_eva_graph.png'

    main(input_file, output_file, graph_file)