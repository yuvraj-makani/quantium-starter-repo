import pandas as pd
import os

# Define file paths
data_folder = "data"
file_names = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

# Initialize an empty list to store dataframes
dfs = []

# Process each file
for file in file_names:
    file_path = os.path.join(data_folder, file)
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Filter for "Pink Morsels"
    df = df[df["product"] == "Pink Morsels"]
    
    # Compute sales (quantity * price)
    df["sales"] = df["quantity"] * df["price"]
    
    # Select only the required columns
    df = df[["sales", "date", "region"]]
    
    # Append to list
    dfs.append(df)

# Combine all dataframes
final_df = pd.concat(dfs, ignore_index=True)

# Save to a new CSV file
output_file = os.path.join(data_folder, "formatted_sales_data.csv")
final_df.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")
