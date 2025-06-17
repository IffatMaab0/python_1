
# Author: Iffat Maab
# Date: 2025-06-12
# Description: A console-based system to add, remove, display, and return books using object-oriented programming.

class library:
    def __init__(self):
        self.books =["Python Basics", "C++ Fundamentals","Data Structures"]
    def add_book(self,book):
        self.books.append(book)
        print(f"{book} has been added!")
    def display_book(self):
        for book in self.books:
            print(book)
    def remove_book(self,book):   
        if book in self.books:
            self.books.remove(book)
            print(f"{book} has been borrowed!")
        else:
            print(f"{book} doesn't exist!")  
    def return_book(self,book):
        self.books.append(book)
        print(f"{book} has been returned")
lib=library()        
def main():
    while True: 
            print(f"Type 1 to add book..")
            print(f"Type 2 to see book..")
            print(f"Type 3 to borrow book..")
            print(f"Type 4 to return book..")
            print(f"Type 5 to  exit..")
            choice = int(input("Enter your choice (1-5): "))
            if(choice==1):
                book=input("Enter the name of book to add: ")
                lib.add_book(book)
            elif(choice==2):
                lib.display_book()
            elif(choice ==3):
                book=input("Enter the name of book to Borrow: ")
                lib.remove_book(book)
            elif(choice==4):
                book=input("Enter the name of book to Return: ")
                lib.return_book(book)
            else:
                print("Invalid Choice!") 
main()                   


                    



