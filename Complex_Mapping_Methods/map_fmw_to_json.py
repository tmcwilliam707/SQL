import xml.etree.ElementTree as ET
import json

def convert_fmw_to_json(fmw_file_path, json_file_path):
    # Parse the FME Workbench (FMW) file
    tree = ET.parse(fmw_file_path)
    root = tree.getroot()
    
    # Function to recursively convert XML to dictionary
    def xml_to_dict(element):
        data_dict = {element.tag: {} if element.attrib else None}
        children = list(element)
        if children:
            dd = {}
            for dc in map(xml_to_dict, children):
                for k, v in dc.items():
                    if k in dd:
                        if not isinstance(dd[k], list):
                            dd[k] = [dd[k]]
                        dd[k].append(v)
                    else:
                        dd[k] = v
            data_dict = {element.tag: dd}
        if element.attrib:
            data_dict[element.tag].update(('@' + k, v) for k, v in element.attrib.items())
        if element.text:
            text = element.text.strip()
            if children or element.attrib:
                if text:
                    data_dict[element.tag]['#text'] = text
            else:
                data_dict[element.tag] = text
        return data_dict
    
    # Convert the XML root to a dictionary
    fmw_dict = xml_to_dict(root)
    
    # Serialize the dictionary to JSON
    with open(json_file_path, 'w') as json_file:
        json.dump(fmw_dict, json_file, indent=4)

# Example usage
fmw_file_path = '/Users/taylormcwilliam/Desktop/IRL_Maintenance_complexparsing_Copy.fmw'
json_file_path = '/Users/taylormcwilliam/Desktop/IRL_Maintenance_complexparsing_Copy.json'
convert_fmw_to_json(fmw_file_path, json_file_path)