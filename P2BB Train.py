import os
import json
import re

# Define input and output folders
input_folder = r"F:\1911331642\CSE499\DATASET\jsonlabels"
output_folder = r"F:\1911331642\CSE499\DATASET\labelsBB"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def extract_bounding_boxes(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Initialize a list to store bounding box annotations
    bounding_boxes = []

    # Iterate through the xy features
    for feature in data['features']['xy']:
        properties = feature['properties']
        subtype = properties['subtype']
        uid = properties['uid']
        wkt = feature['wkt']

        # Extract coordinates from the WKT string with error handling
        matches = re.findall(r"-?\d+\.\d+", wkt)
        
        # Check if there are enough coordinates to form a bounding box
        if len(matches) < 4:
            # There should be at least 4 coordinates to define a bounding box
            print(f"Skipping invalid data for uid: {uid}")
            continue

        coords = [float(match) for match in matches]

        # Split the coordinates into x and y pairs
        polygon_coords = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]

        # Calculate the bounding box coordinates
        min_x = min(coord[0] for coord in polygon_coords)
        max_x = max(coord[0] for coord in polygon_coords)
        min_y = min(coord[1] for coord in polygon_coords)
        max_y = max(coord[1] for coord in polygon_coords)

        # Create a bounding box annotation
        bounding_box = {
            'uid': uid,
            'subtype': subtype,
            'min_x': min_x,
            'max_x': max_x,
            'min_y': min_y,
            'max_y': max_y,
        }

        # Append the bounding box to the list
        bounding_boxes.append(bounding_box)

    return bounding_boxes

# Iterate through JSON files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        # Extract bounding box information from the input JSON file
        bounding_boxes_data = extract_bounding_boxes(input_file_path)

        # Write the bounding box data to the output JSON file
        with open(output_file_path, 'w') as output_json_file:
            json.dump(bounding_boxes_data, output_json_file, indent=2)

        print(f'Processed: {filename}')

print('Bounding box extraction and JSON file creation completed.')


