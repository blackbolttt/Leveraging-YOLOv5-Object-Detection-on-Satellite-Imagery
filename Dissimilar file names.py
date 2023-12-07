import os

# Define the paths to your JSON and PNG file directories
json_dir = r"C:\Users\User\Desktop\train\POST DATASET\labelsyolo"
png_dir = r"C:\Users\User\Desktop\train\POST DATASET\Images"

# Get the list of JSON and PNG files without extensions
json_files = set([os.path.splitext(filename)[0] for filename in os.listdir(json_dir) if filename.endswith('.txt')])
png_files = set([os.path.splitext(filename)[0] for filename in os.listdir(png_dir) if filename.endswith('.png')])

# Find dissimilar JSON and PNG files
dissimilar_json_files = json_files - png_files
dissimilar_png_files = png_files - json_files

# Save dissimilar JSON and PNG file names to text files
with open('dissimilar_json_files.txt', 'w') as file:
    for file_name in dissimilar_json_files:
        file.write(file_name + '.json\n')

with open('dissimilar_png_files.txt', 'w') as file:
    for file_name in dissimilar_png_files:
        file.write(file_name + '.png\n')

print("Dissimilar JSON file names saved to 'dissimilar_json_files.txt'")
print("Dissimilar PNG file names saved to 'dissimilar_png_files.txt'")
