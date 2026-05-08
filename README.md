# Spacewalks

## Overview

Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation

## Installation

`Spacewalks` depends on `pandas` and `matplotlib.pyplot`. It has been developed using `python3.12`. It is recommended that you create a new virtual environment with 

`python -m venv <name>`

before installing the dependencies using the provided `requirements.txt` file

`python -m pip install -r requirements.txt`

## Usage

`python eva_data_analysis.py`

`pytest`