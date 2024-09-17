import os
import pandas as pd

data_dir = 'data'

def list_directory_structure(startpath):
    structure = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            structure.append(f"{subindent}{f}")
    return '\n'.join(structure)

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    print(f"Contents of {file_path}:")
    print(df.head())

if __name__ == "__main__":
    structure = list_directory_structure(data_dir)
    print("Directory structure of 'data':")
    print(structure)
    
    # Define the path to the CSV file
    csv_file_path = os.path.join(data_dir, 'mturkfitbit_export_3.12.16-4.11.16', 'Fitabase Data 3.12.16-4.11.16', 'weightLogInfo_merged.csv')
    
    # Check if the file exists
    if os.path.exists(csv_file_path):
        read_csv_file(csv_file_path)
    else:
        print(f"File {csv_file_path} does not exist.")