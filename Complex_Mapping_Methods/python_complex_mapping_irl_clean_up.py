import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = '/Users/taylormcwilliam/Downloads/684876121227919360/files/APPL_CSV_Q423/Address_Model.csv'

# Read the first 100 rows of the CSV file
chunk_size = 100
df_chunk = pd.read_csv(file_path, encoding='latin1', nrows=chunk_size)

# Specify the path for the new CSV file
output_file_path = '/Users/taylormcwilliam/Downloads/684876121227919360/files/APPL_CSV_Q423/Address_Model_chunk.csv'

# Write the chunk to a new CSV file
df_chunk.to_csv(output_file_path, index=False)

print(f"First {chunk_size} rows have been written to {output_file_path}")