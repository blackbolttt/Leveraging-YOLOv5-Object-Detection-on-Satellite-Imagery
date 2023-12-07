import os
import json

# Define class names
class_names = {
    "no-damage": 0,
    "minor-damage": 1,
    "major-damage": 2,
    "destroyed": 3,
    "un-classified": 4,
}

# Input and output folders
json_folder = r"F:\1911331642\CSE499\Final Work\labelsBB"
yolo_folder = r"F:\1911331642\CSE499\Final Work\labels"

# Ensure the output folder exists
os.makedirs(yolo_folder, exist_ok=True)

# Function to convert JSON to YOLO format
def json_to_yolo(json_data):
    x_min = abs( json_data["min_x"] )
    x_max = abs( json_data["max_x"] )
    y_min = abs( json_data["min_y"] )
    y_max = abs( json_data["max_y"] )

    x_center = abs((x_min + x_max) / (2*1024) )
    y_center = abs((y_min + y_max) / (2*1024) )
    width = abs((x_max - x_min) / 1024 )
    height = abs((y_max - y_min) / 1024 )

    class_index = class_names.get(json_data["subtype"])
    if class_index is None:
        raise ValueError(f"Unknown class: {json_data['subtype']}")

    return f"{class_index} {x_center} {y_center} {width} {height}"

# Process JSON files in the input folder
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        # Read JSON file
        with open(os.path.join(json_folder, filename), "r") as json_file:
            data = json.load(json_file)

        # Create YOLO label file
        yolo_filename = os.path.splitext(filename)[0] + ".txt"
        yolo_filepath = os.path.join(yolo_folder, yolo_filename)

        # Convert and write data in YOLO format
        with open(yolo_filepath, "w") as yolo_file:
            for item in data:
                yolo_line = json_to_yolo(item)
                yolo_file.write(yolo_line + "\n")

print("Conversion complete.")
