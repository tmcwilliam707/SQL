import pandas as pd

def check_null_geometry_and_count_unique_ids(file_path):
    # Load the data into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check for rows with null values in the 'geometry' column
    null_geometry_rows = df[df['GEOMETRY'].isnull()]
    
    # Output the result for null geometry
    if not null_geometry_rows.empty:
        print("Rows with null values in 'geometry' column:")
        print(null_geometry_rows)
    else:
        print("No rows with null values in 'geometry' column.")
    
    # Count unique feature_id values
    unique_feature_ids_count = df['FEATURE_ID'].nunique()
    print(f"Total unique feature_id values: {unique_feature_ids_count}")

# Example usage
file_path = '/Users/taylormcwilliam/Desktop/Source Integration/complete_irl_post_sub_district.csv'
check_null_geometry_and_count_unique_ids(file_path)