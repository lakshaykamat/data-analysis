# %% [markdown]
# # Data Cleaning Pipeline
# This notebook outlines a structured process for cleaning, transforming, and preparing app usage data for analysis. 
# The steps include removing unwanted text, converting time formats, reshaping data, and merging datasets.
#
# ---
#
# ## Step 1: Import Libraries

# %%
import pandas as pd
import re
import numpy as np

# %% [markdown]
# ## Step 2: Load the Dataset
# Load the primary dataset containing app usage data.

# %%
# File paths
file_path = "StayFree Export - Total Usage - 12_19_24.xls"  # Replace with your actual file path
output_path = "usage_data_cleaned.xlsx"

# Load the dataset
usage_time_df = pd.read_excel(file_path, sheet_name="Usage Time")
usage_time_df.head()

# %% [markdown]
# ## Step 3: Remove Dynamic Text Information
# Define a function to clean dynamic text, such as creation dates and app metadata.

# %%
# Function to remove dynamic creation info
def remove_creation_info(text):
    if isinstance(text, str):
        text = re.sub(r"Creation date:\s*\d{1,2}/\d{1,2}/\d{2,4}\s*\d{1,2}:\d{2}:\d{2}(:\d{2})?", '', text)
        text = re.sub(r"Created by \u201cStayFree\u201d\.", '', text)
    return text

# Apply the function to clean the dataset
usage_time_df = usage_time_df.applymap(remove_creation_info)
usage_time_df.columns.values[0] = 'Apps'

# %% [markdown]
# ## Step 4: Clean Unwanted Columns
# Remove columns with irrelevant data (e.g., `Unnamed` or `Device`) to streamline the dataset.

# %%
# Remove unwanted columns
usage_time_df = usage_time_df.loc[:, ~usage_time_df.columns.str.contains('^Unnamed')]
usage_time_df = usage_time_df.loc[:, ~usage_time_df.columns.str.contains('Device')]

# %% [markdown]
# ## Step 5: Convert Time to Hours
# Define a function to standardize various time formats (e.g., `3h 4m`, `29m`) into total hours.

# %%
# Function to convert time strings to hours
def convert_to_hours(time_str):
    if pd.isna(time_str) or time_str == '0s':
        return 0.0

    hours = minutes = seconds = 0
    
    match = re.match(r'(\d+)h\s*(\d+)m\s*(\d+)s', time_str)
    if match:
        hours, minutes, seconds = int(match.group(1)), int(match.group(2)), int(match.group(3))
    else:
        match = re.match(r'(\d+)h\s*(\d+)m', time_str)
        if match:
            hours, minutes = int(match.group(1)), int(match.group(2))
        else:
            match = re.match(r'(\d+)m\s*(\d+)s', time_str)
            if match:
                minutes, seconds = int(match.group(1)), int(match.group(2))
            else:
                match = re.match(r'(\d+)m', time_str)
                if match:
                    minutes = int(match.group(1))
                else:
                    match = re.match(r'(\d+)s', time_str)
                    if match:
                        seconds = int(match.group(1))

    return hours + (minutes / 60) + (seconds / 3600)

# Test the function
convert_to_hours("29m")

# %% [markdown]
# ## Step 6: Clean DataFrame
# Remove rows with `Total Usage`, empty values, or NaN entries.

# %%
# Clean the data
usage_time_cleaned = usage_time_df.drop('Total Usage', axis=1, errors='ignore')
usage_time_cleaned = usage_time_cleaned.dropna(how='any')
usage_time_cleaned = usage_time_cleaned.loc[~(usage_time_cleaned == '').any(axis=1)]
usage_time_cleaned = usage_time_cleaned[usage_time_cleaned['Apps'] != 'Total Usage']

# %% [markdown]
# ## Step 7: Reshape DataFrame to Long Format
# Transform the data from a wide format (dates as columns) to a long format.

# %%
# Convert to long format
usage_time_long = pd.melt(usage_time_cleaned, id_vars=['Apps'], var_name='Date', value_name='Usage')

# %% [markdown]
# ## Step 8: Convert Date Column
# Standardize the `Date` column to ISO format (`YYYY-MM-DD`).

# %%
# Format the Date column
usage_time_long['Date'] = pd.to_datetime(usage_time_long['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# %% [markdown]
# ## Step 9: Convert Usage Column to Hours
# Apply the `convert_to_hours` function to the `Usage` column.

# %%
# Convert usage to hours
usage_time_long['Usage (in hours)'] = usage_time_long['Usage'].apply(convert_to_hours)

# %% [markdown]
# ## Step 10: Add Usage Count Data
# Load usage count data and merge it with the cleaned dataset.

# %%
# Load and clean usage count data
usage_count_df = pd.read_excel(file_path, sheet_name="Usage Count")
usage_count_df = usage_count_df.applymap(remove_creation_info)
usage_count_df = usage_count_df.loc[~(usage_count_df == '').any(axis=1)]
usage_count_df = usage_count_df.drop(columns=['Device'], errors='ignore')
usage_count_df = usage_count_df.dropna()
usage_count_df.rename(columns={usage_count_df.columns[0]: 'App Name'}, inplace=True)
usage_count_df = usage_count_df[usage_count_df['App Name'] != 'Total Usage']

# Reshape to long format
usage_count_long = usage_count_df.melt(id_vars=['App Name'], var_name='Date', value_name='Usage Count')
usage_count_long['Date'] = pd.to_datetime(usage_count_long['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Merge with the main dataset
merged_df = pd.merge(usage_time_long, usage_count_long, left_on=['Apps', 'Date'], right_on=['App Name', 'Date'], how='left')
merged_df = merged_df.drop(columns=['App Name']).fillna({'Usage Count': 0})

# %% [markdown]
# ## Step 11: Add Device Unlock Data
# Load and merge device unlock data into the main dataset.

# %%
# Load and clean unlock data
unlock_df = pd.read_excel(file_path, sheet_name="Device Unlocks")
unlock_df = unlock_df.applymap(remove_creation_info)
unlock_df = unlock_df.drop(columns=['Unlock', 'Total Usage'], errors='ignore')

# Reshape unlock data
unlock_long = unlock_df.melt(var_name="Date", value_name="Device Unlock")
unlock_long["Date"] = pd.to_datetime(unlock_long["Date"], format="%B %d, %Y").dt.strftime("%Y-%m-%d")

# Merge unlock data
merged_df = pd.merge(merged_df, unlock_long, on="Date", how="left")
merged_df["Device Unlock"] = merged_df["Device Unlock"].fillna(0)

# %% [markdown]
# ## Step 12: Save the Cleaned Data
# Save the final cleaned dataset to an Excel file.

# %%
# Save the final DataFrame
merged_df.to_excel(output_path, index=False)
merged_df.head()
