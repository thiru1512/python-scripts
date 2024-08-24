import os

def list_dir(value):
    try:
        files = os.listdir(value)
        return files,None
    except FileNotFoundError:
        return None,"Folder not found"
    

def main():
    folders_path = input("Enter the folder name with spaces:").split()
    for folder_path in folders_path:
        files,error = list_dir(folder_path)   
        if files:
            print(f"files in {folder_path}")
            for file in files:
                print(file)
        else:
            print(f"error in {folder_path} {error}")

main()