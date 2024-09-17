import os

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

if __name__ == "__main__":
    structure = list_directory_structure(data_dir)
    print("Directory structure of 'data':")
    print(structure)