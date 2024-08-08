import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = '/Users/taylormcwilliam/Documents/irl_csr_postal_sub_district.csv'

# Read the CSV file into a DataFrame without headers
df = pd.read_csv(csv_file_path, header=None)

# Assign a column name to the single column
df.columns = ['feature_id']

# Find duplicate feature_id values
duplicate_feature_ids = df[df.duplicated('feature_id', keep=False)]

# Print the duplicate feature_id values
if not duplicate_feature_ids.empty:
    print("Duplicate feature_id values found:")
    print(duplicate_feature_ids)
else:
    print("No duplicate feature_id values found.")