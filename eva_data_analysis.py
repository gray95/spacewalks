import csv
import json
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    print(f"reading JSON file: {input_file}")
    df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    df['eva'] = df['eva'].astype(float)
    # remove rows which don't have duration or date entries
    df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return df

def write_dataframe_to_csv(df, output_file):
    print(f"converting json to csv and writing to: {output_file}")
    df.to_csv(output_file, index=False, encoding='utf-8')

def plot_cumulative_time_in_space(df, graph_file):
    # plot cumulative eva time against date
    print("plotting cumulative time in space")
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

print("--START--")

# read data from JSON file
eva_data = read_json_to_dataframe(input_file)

# convert and export data to csv
write_dataframe_to_csv(eva_data, output_file)

eva_data.sort_values('date', inplace=True)

# calculate eva durations in hours and the cumulative eva time 
# and store them in the same dataframe.
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()

plot_cumulative_time_in_space(eva_data, graph_file)

print("--END--")