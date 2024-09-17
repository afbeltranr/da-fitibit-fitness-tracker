import os
import pandas as pd

data_dir = 'data'

def show_head_of_first_csv():
    print("Starting the script...")
    
    if not os.path.exists(data_dir):
        print(f"Data directory '{data_dir}' does not exist.")
        return False
    
    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    if not folders:
        print("No folders found in the data directory.")
        return False
    
    first_folder = folders[0]
    csv_files = [f for f in os.listdir(os.path.join(data_dir, first_folder)) if f.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the first folder.")
        return False
    
    first_csv = csv_files[0]
    df = pd.read_csv(os.path.join(data_dir, first_folder, first_csv))
    output = df.head().to_string()
    print(output)
    
    # Ensure the /app directory exists
    os.makedirs('/app', exist_ok=True)
    
    with open('/app/output.txt', 'w') as f:
        f.write(output)
    
    print("Output written to /app/output.txt")
    return True

if __name__ == "__main__":
    if show_head_of_first_csv():
        print("Test passed.")
    else:
        print("Test failed.")
        exit(1)