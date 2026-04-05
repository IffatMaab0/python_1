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
            f.write(content)
            print (f"Data added to the {filename}")
    except FileNotFoundError:
        print(f"{filename} not found")
    except Exception as e:
        print("An Error Occured!")  

def main():
    while True:
        print("--File Management System--")
        print("Type 0 --> To Exit The System")
        print("Type 1 --> To Create File")
        print("Type 2 --> To View All Files")
        print("Type 3 --> To Delete File")
        print("Type 4 --> To Read File")
        print("Type 5 --> To Rewrite File")

        choice = input("Type your choice(0-6): ")

        if choice == "0":
            print("Exiting..")
            break

        elif choice == "1":
            filename = input("Type the File-Name to create: ")
            create_file(filename)

        elif choice == "2":
            view_all_files() 

        elif choice == "3":
            filename = input("Type the File-Name to Delete: ") 
            delete_file(filename) 

        elif choice == "4":
            filename = input("Type the File-Name to Read: ")   
            read_file(filename)

        elif choice == "5":
            filename = input("Type the File-Name to Write: ") 
            rewrite_file(filename)  
        else:
            print("In-Valid Syntax!")

if __name__ =="__main__"  :
    main()              




