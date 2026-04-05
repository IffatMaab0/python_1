import os

def create_file(filename):
    try:
        with open(filename, 'x'):
            print(f"{filename}: was created successfully!")
    except FileExistsError:
        print(f"{filename} Already exists!")
    except Exception as E:
        print("An Error Occured!")

def view_all_files():
    files = os.listdir
    if not files:
        print("No file found!")
    else:    
        print("files in directory")
        for file in files:
            print(file)

def delete_file(filename)  :
    try:
        os.remove(filename) 
        print(f"{filename} was deleted successfully!")
    except FileNotFoundError:
        print("{filename} not found!") 
    except Exception as e:
        print("An Error Occured!")  

def read_file(filename):
    try:
        with open(filename , "r") as f:
            content = f.read
            print(f"the content of file is: \n{content}" )
    except FileNotFoundError:
        print(f"{filename} not found!")    

    except Exception as e:
        print("An Error Occured")        
            
def rewrite_file(filename):
    try:
        with open (filename , "w") as f:
            content = input("Type to Add data: ")
            f.write(content )
            print ( f "\n Data added to the {filename}")
    except FileNotFoundError:
        print(f"{filename} not found")
    except Exception as e:
        print("An Error Occured!")  

d          

