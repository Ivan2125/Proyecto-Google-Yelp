import pandas as pd
import numpy as np
import re
from pathlib import Path
from datetime import datetime

directorio = Path("data/Google Maps/reviews-estados")
output_directory = Path("state_parquet")


# Function to convert None values to 'No' and other values to 'Yes'
def replace_none(value):
    if value is None:
        return "No"
    else:
        return "Yes"


# Iterate over each folder in the base directory
for folder_path in directorio.iterdir():
    # Check if the item in the base directory is a folder
    if folder_path.is_dir():
        # Generator to store the individual DataFrames
        dfs = (
            pd.read_json(json_file, lines=True)
            for json_file in folder_path.glob("*.json")
        )

        # Concatenate all DataFrames into one
        df_combined = pd.concat(dfs, ignore_index=True)

        # Define the output file path
        output_file_path = output_directory / f"df_{folder_path.name}.parquet"

        # Store the DataFrame as a Parquet file
        df_combined.to_parquet(output_file_path, index=False)

        # Print a message confirming the storage location
        print(
            f"The combined DataFrame for {folder_path.name} was saved in {output_file_path}"
        )

# Path to the directory containing the dataframes
input_directory = Path("state_parquet")
output_directory = Path("filtered_df")

sitios_metadata = Path(
    "data/Google Maps/metadata-sitios/df_convenience_clean_1.parquet"
)

df_sitios = pd.read_parquet(sitios_metadata)

# Iterate over each file in the input directory
for parquet_file in input_directory.glob("*.parquet"):
    # Read the DataFrame from the Parquet file
    df = pd.read_parquet(parquet_file)

    df["resp"] = df["resp"].apply(replace_none)

    # Perform information of each dataframe
    # Drop columns pics and resp
    df.drop(["pics"], axis=1, inplace=True)
    # Eliminate duplicate records
    df.drop_duplicates(inplace=True)

    # Merge dfreviewsGoogle1 and df_sitios based on the 'gmap_id' column
    df = df.merge(
        df_sitios[["gmap_id", "name", "category", "city"]], on="gmap_id", how="left"
    )

    # Rename the 'name_y' column from df_sitios to 'business_name' in the merged DataFrame
    df.rename(columns={"name_y": "business_name", "name_x": "name"}, inplace=True)

    # Drop rows with NaN values in 'business_name', 'City', and 'State' columns
    df = df.dropna(subset=["business_name", "city"])

    # Extract the state name from the filename
    state_name = parquet_file.stem.split("-")[-1]

    # Add a new column 'State_review' with the state name to the DataFrame
    df["state_review"] = state_name

    # Store the transformed DataFrame in the output directory
    output_file_path = output_directory / parquet_file.name
    df.to_parquet(output_file_path, index=False)

    # Print a message confirming the storage location
    print(
        f"The transformed DataFrame for {parquet_file.name} was saved in {output_file_path}"
    )

# Path to the directory containing the filtered DataFrames
input_directory = Path("filtered_df")

# Generator to store the DataFrames
dfs = (
    pd.read_parquet(parquet_file) for parquet_file in input_directory.glob("*.parquet")
)

# Concatenate all DataFrames into one
df_Google_reviews_CS = pd.concat(dfs, ignore_index=True)

# Print information about the resulting DataFrame
print("Combined DataFrame shape:", df_Google_reviews_CS.shape)
print("Combined DataFrame head:")
print(df_Google_reviews_CS.head())

df_Google_reviews_CS.to_parquet("filtered_df/df_Google_reviews_CS.parquet")
