import sys

def update_file(file_path,key,value):
    try:
        with open(file_path,'r') as file1:
            lines = file1.readlines()
        with open(file_path,'w') as file2:
            for line in lines:
                if key in line:
                    file2.write(key + " = " + value + "\n")
                else:
                    file2.write(line)
            print(f"{file_path} file updated successfully")
    except FileNotFoundError:
        print(f"{file_path} not found")
        
file_pat = sys.argv[1]
ke = sys.argv[2]
valu = sys.argv[3]

update_file(file_pat,ke,valu)