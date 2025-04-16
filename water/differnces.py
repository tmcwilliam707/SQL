import pandas as pd

# Load the old repo CSV
old_df = pd.read_csv('/Users/taylormcwilliam/Downloads/MUNI AND CITY ITA.sql.csv')

# Load the new repo CSV
new_df = pd.read_csv('/Users/taylormcwilliam/Downloads/MUNI AND CITY VENDOR REFRESH.csv')

# Inspect the data to ensure the columns are as expected
print(old_df.head())
print(new_df.head())

# Merge old and new repositories on feature_id
merged_df = pd.merge(old_df, new_df, on='FEATURE_ID', suffixes=('_old', '_new'))

# View the merged dataframe
print(merged_df.head())

# Compare Territory_Name
merged_df['name_difference'] = merged_df['TERRITORY_NAME_old'] != merged_df['TERRITORY_NAME_new']

# Compare Geometry (assuming it's stored as a simple string for now)
merged_df['geometry_difference'] = merged_df['GEOMETRY_old'] != merged_df['GEOMETRY_new']

# Filter only rows where there are differences
differences_df = merged_df[(merged_df['name_difference']) | (merged_df['geometry_difference'])]

# View the differences
print(differences_df.head())

# Save the differences to a CSV report
differences_df.to_csv('/Users/taylormcwilliam/Downloads/territory_differences_report.csv', index=False)
