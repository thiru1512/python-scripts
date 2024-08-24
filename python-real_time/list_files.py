import os
folder_list_name = input("enter the folders with spaces:").split()


for folder in folder_list_name:
    try:
        folders_list = os.listdir(folder)
    except FileNotFoundError:
        print(f"Incorrect foldername {folder}")
        continue
    except PermissionError:
        print(f"dont have permission to list {folder}")
        continue
    print("----List of files in folder-----")
    print(folder)
    print("**************************************")
    for file in folders_list:
        print(file)
                   
    print("**************************************")