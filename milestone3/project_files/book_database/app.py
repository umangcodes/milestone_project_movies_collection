"""
Project name: milestone project 3

Author: Umang A
Start date: 15 May 2020 1530
Description: Book database with file I/O
Release date:
    version 1.0: 15 May 2020 1815
    version 2.0: in progress
    version 3.0: not related

Modified: None
Version 1.0 :
basic functionality of creating a list of dictonaries containing the information of the books in a structured manner.
structure of the list will be as follows:
    [
    ("Name": ,"Author": ,"Status": ),
    ("Name": ,"Author": ,"Status": ),
    ("Name": ,"Author": ,"Status": )
    ]

version 2.0:
==> search for books using
                        book title
                        book author
                        book status
==> view books by
                author
                status
==> remove books by
                    name
                    author
                    status
version 3.0:
permanent storage
"""



"""
========================================================================================================================
                                                    Data Ops
========================================================================================================================
"""
print('''Hello Sir, welcome to your personal book database. 
    Initiating, please wait......''')
book_database = []
def continue_operation():
    while True:
        operation = input("continue operation:\n=>")
        if operation == "Y" or operation == "y" or operation == "Yes" or operation == "YES":
            return True
        elif operation == "N" or operation == "n" or operation == "No" or operation == "NO":
            return False
        else:
            print(f"Invalid Command: {operation}")

def add_books_to_database():
    adding = 1
    while adding:
        book_name = input("Please enter the name of the book: ")
        book_author = input("Please enter book author: ")
        book_status = input("have you read this book?(y/n): ")  # check for the type of the input from the user, valid inputs( y, n, Y, N, Yes, YES, No, NO)
        book_database.append({"Name":book_name,"Author":book_author,"Status":book_status})
        user_choice = continue_operation()
        if user_choice == True:
            adding = 1
        else:
            if user_choice == False:
                print("terminating operation!")
            else:
                print(user_choice)
            adding = 0
def view_database():
    view_method = input()
    for book_data in book_database:
        book_name = book_data["Name"]
        book_author = book_data["Author"]
        book_status = book_data["Status"]
        print(f"Book Title: {book_name.title()} \t|| Book Author: {book_author.title()} \t|| Read: {book_status.title()}")

def search_database():
    #opeartion extension in next version with
    #search_option = input("By author or by title: ")
    #search option not implemented
    #copy the index to a list so that the user will not need to write it down for future reference.
    search_parameter = input("Input the title name: \n=> ")
    for book in book_database:
        if book["Name"] == search_parameter:
            book_location = book_database.index(book) + 1
            print(f"Title found in the database. \n\tLocation: {book_location}")
            return book
    else:
        print("Ghhh!!! Book not found! Please try other options.")

def remove_book_from_database():
    removing_content = True
    while removing_content:
        book_location = search_database()
        book_database.remove(book_location)
        user_choice = continue_operation()
        if user_choice == True:
            removing_content = True
        else:
            if user_choice == False:
                print("terminating operation!")
            else:
                print(user_choice)
            removing_content = 0

def user_menu():
    terminate_program = False
    while not terminate_program:
        user_choice = input("""What will you like me to do for you?
1.) press A: To add books to database 
2.) press V: To view database
3.) press S: To find books from the database
4.) press R: To remove books from the database
5.) press Q: To terminate program execution  \n=> """)
        if user_choice == "A" or user_choice == "a" or user_choice == "Add" or user_choice == "ADD":
            add_books_to_database()
        elif user_choice == "V" or user_choice == "v" or user_choice == "View" or user_choice == "VIEW":
            view_database()
        elif user_choice == "S" or user_choice == "s" or user_choice == "Search" or user_choice == "SEARCH":
            search_database()
        elif user_choice == "R" or user_choice == "r" or user_choice == "Remove" or user_choice == "REMOVE":
            remove_book_from_database()
        elif user_choice == "V" or user_choice == "v" or user_choice == "View" or user_choice == "VIEW":
            view_database()
        elif user_choice == "Q" or user_choice == "q" or user_choice == "Quit" or user_choice == "QUIT":
            terminate_program = True
        else:
            print("Invalid command")

"""
========================================================================================================================
                                                    MAIN Execution
========================================================================================================================
"""
user_menu()