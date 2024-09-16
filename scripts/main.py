import os
import pandas as pd

def show_head_of_first_csv(data_dir='data'):
    # List all folders in the data directory
    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    
    if not folders:
        print("No folders found in the data directory.")
        return
    
    # Get the first folder
    first_folder = folders[0]
    first_folder_path = os.path.join(data_dir, first_folder)
    
    # List all files in the first folder
    files = [f for f in os.listdir(first_folder_path) if os.path.isfile(os.path.join(first_folder_path, f))]
    
    if not files:
        print("No files found in the first folder.")
        return
    
    # Get the first file
    first_file = files[0]
    first_file_path = os.path.join(first_folder_path, first_file)
    
    # Read the CSV file
    df = pd.read_csv(first_file_path)
    
    # Show the head of the dataset
    print(df.head())

if __name__ == "__main__":
    show_head_of_first_csv()