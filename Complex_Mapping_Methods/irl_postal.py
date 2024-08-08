import json

def count_geojson_features(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if 'features' in data:
            return len(data['features'])
        else:
            return 0

# Example usage
file_path = '/Users/taylormcwilliam/Desktop/IRL_Address_Derived_Territory/IRL_POSTAL_CITY.geojson'
num_features = count_geojson_features(file_path)
print(f'Number of features in the GeoJSON file: {num_features}')

file_path = '/Users/taylormcwilliam/Desktop/IRL_Address_Derived_Territory/IRL_POSTAL_DISTRICT.geojson'
num_features = count_geojson_features(file_path)
print(f'Number of features in the GeoJSON file: {num_features}')

file_path = '/Users/taylormcwilliam/Desktop/IRL_Address_Derived_Territory/IRL_POSTAL_SUB_DISTRICT.geojson'
num_features = count_geojson_features(file_path)
print(f'Number of features in the GeoJSON file: {num_features}')

import json

def list_geojson_fields(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if 'features' in data:
            fields = set()
            for feature in data['features']:
                if 'properties' in feature:
                    fields.update(feature['properties'].keys())
            return fields
        else:
            return set()

# Example usage
file_paths = [
    '/Users/taylormcwilliam/Desktop/IRL_Address_Derived_Territory/IRL_POSTAL_CITY.geojson',
    '/Users/taylormcwilliam/Desktop/IRL_Address_Derived_Territory/IRL_POSTAL_DISTRICT.geojson',
    '/Users/taylormcwilliam/Desktop/IRL_Address_Derived_Territory/IRL_POSTAL_SUB_DISTRICT.geojson'
]

for file_path in file_paths:
    fields = list_geojson_fields(file_path)
    print(f'Fields in {file_path}: {fields}')