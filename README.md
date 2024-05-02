# CITS1401 Python Project: Population Data Analysis

## Project Overview

This project, authored by Wiz Zhang (SID:23210735), comprises a Python program that processes population data from a CSV file. The script performs multiple analyses based on a given region, producing several key statistics that include the minimum and maximum population countries, average and standard deviation of the population, population density calculations, and correlation between population and land area.

## Key Features

1. **Minimum and Maximum Population Identification**:
   - Identifies the countries with the minimum and maximum population within a specified region where the net change in population is positive.

2. **Population Statistics**:
   - Calculates both the average and standard deviation of the population for a specified region.

3. **Population Density**:
   - Computes the population density for each country within a specified region.

4. **Population and Land Area Correlation**:
   - Determines the correlation between the population and land area for all countries in a specified region.

## Efficiency
To optimize performance, the script minimizes the number of loops by calculating multiple statistics within the same iteration over the data, rather than dividing these tasks into separate functions.

## Code Example

The `main` function serves as the entry point of the program, orchestrating the data processing by invoking the `process_data` function. Here's a brief look at how the functions are structured:

```python
def main(csvfile, region):
    MaxMin, stdvAverage, density, corr = process_data(csvfile, region)
    return MaxMin, stdvAverage, density, corr

def process_data(csvfile, region):
    with open(csvfile, 'r', encoding='utf-8') as file:
        data = file.readlines()
    # Data processing logic follows
