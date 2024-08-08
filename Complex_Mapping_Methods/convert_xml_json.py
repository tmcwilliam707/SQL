import xml.etree.ElementTree as ET
import json

def parse_xml_to_json(xml_file):
    try:
        with open(xml_file, 'r') as file:
            content = file.read()
            print("XML Content:\n", content)  # Debugging step to print the content

        # Check if the content is empty
        if not content.strip():
            print("Error: The XML file is empty.")
            return {}

        tree = ET.ElementTree(ET.fromstring(content))
        root = tree.getroot()

        nodes = []
        edges = []

        for node in root.findall('.//node'):
            node_id = node.get('id')
            node_type = node.get('type')
            node_setting = {}

            for setting in node:
                if setting.tag == 'setting':
                    for item in setting:
                        if item.tag == 'name':
                            node_setting['name'] = item.text
                        elif item.tag == 'alias':
                            node_setting['alias'] = item.text
                        elif item.tag == 'mapping_rule':
                            node_setting['mapping_rule'] = parse_mapping_rule(item)
                        # Add more settings as needed

            nodes.append({
                'node_id': node_id,
                'node_type': node_type,
                'node_setting': node_setting
            })

        for edge in root.findall('.//edge'):
            source = edge.get('source')
            target = edge.get('target')
            edges.append({
                'source': source,
                'target': target
            })

        json_data = {
            'node': nodes,
            'edge': edges
        }

        return json_data

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return {}

def parse_mapping_rule(mapping_rule_element):
    # Implement parsing logic for mapping_rule
    # This is a placeholder function
    return {}

xml_file = 'irl_man_complex_parsing.xml'
json_data = parse_xml_to_json(xml_file)

with open('irl_complex_parsing_ndt.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)