import re

# Define the path to your XML file
file_path = 'irl_man_complex_parsing.xml'

# Define the unwanted characters (example: removing all non-alphanumeric characters except for basic XML symbols)
unwanted_chars = re.compile(r'[!#]')

# Read the XML file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Debugging step: Print the original content
print("Original Content:\n", content)

# Strip unwanted characters
cleaned_content = re.sub(unwanted_chars, '', content)

# Ensure the XML declaration is at the beginning
if not cleaned_content.startswith('<?xml'):
    cleaned_content = '<?xml version="1.0" encoding="UTF-8"?>\n' + cleaned_content

# Debugging step: Print the cleaned content
print("Cleaned Content:\n", cleaned_content)

# Write the cleaned content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

print("Unwanted characters have been removed from the XML file.")