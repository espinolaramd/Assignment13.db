#Diego Espinola
#04.29.2020
#This assignment is about Database.I am going to create a Table where the user is going to be able to modify, add and delete data.


import sqlite3
from sqlite3 import Error

def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn




# Create the connection object to the database, "database filename" is the parameter

connection = create_connection("Assignment13.db")



# Execute predefined write queries
# Send the query as a parameter
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


# Execute predefined read queries
# Send the query as a parameter

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip TEXT NOT NULL
);
"""
execute_query(connection,create_customer_table)

create_book_table = """
CREATE TABLE IF NOT EXISTS book (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    ISBN TEXT NOT NULL  ,
    edition TEXT NOT NULL,
    price TEXT NOT NULL,
    publisher TEXT NOT NULL
);
    """
execute_query(connection,create_book_table)
#-----------------------------------------------------------------------#
Menu = 0

while Menu != 3:
    print('1)Customers table')
    print("2)Books table")
    print("3)Exit Program")
    Menu = int(input("Welcome, please choice one of the next options:"))
    if Menu == 1:
        print("Customers menu:")
        print('1)Add a new customer')
        print('2)Modify an existing customer')
        print('3)Print a list of all customers')
        print('4)Delete a customer')
        print('5)Return to main menu')
        option = int(input("\n>"))
        if option == 1:
            print("Please enter the details for the person:")
            first_name = input("What is the first name?")
            last_name = input("What is the last name?")
            street_address = input("What is the street address?")
            city = input("What is the city?")
            state = input("What is the state?")
            zip_code = input("What is the zip code?")

            create_customer = f"""
            INSERT INTO
                 customer (first, last, address, city, state, zip)
            VALUES
                ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip_code}');
            """
            execute_query(connection, create_customer)
        if option == 2:
            print("Please enter the details you want to edit:")
            modify = input()
            print("Please enter the new information:")
            new_information = input()
            print("Please enter the old information")
            old_information = input()


            update_person_name = f"""
            UPDATE
                customer
            SET
                {modify} = '{new_information}'
            WHERE
                {modify} = '{old_information}'
            """

            execute_query(connection, update_person_name)
        if option == 3:
            select_customers = "SELECT * from customer"
            people = execute_read_query(connection, select_customers)

            for person in people:
                print(person)
        if option == 4:
            print("Please enter the details of the costumer you want to delete")
            last_name_delete = input("last name \n> ")
            first_name_delete = input("first name \n>")
            delete_customer = f"""
            DELETE
                customer
            WHERE
                last_name = '{last_name_delete}'
                first_name = '{first_name_delete}'
            """
            execute_query(connection,delete_customer)
            print(f"{first_name_delete}{last_name_delete} was deleted")
    elif Menu == 2:
        print("Books menu:")
        print('1)Add a new book')
        print('2)Modify an existing book')
        print('3)Print a list of all books')
        print('4)Delete a book')
        print('5)Return to main menu')
        option = int(input("\n>"))
        if option == 1:
            print("Please enter the details for the book:")
            title = input("What is the title?")
            author = input("What is the author?")
            ISBN = input("What is the ISBN?")
            edition = input("What is edition?")
            price = input("What is the price?")
            publisher = input("What is the publisher?")

            create_book = f"""
            INSERT INTO
                book (title, author, ISBN, edition, price, publisher)
            VALUES
                ('{title}', '{author}', '{ISBN}', '{edition}', '{price}', '{publisher}');
            """
            execute_query(connection, create_book)

            if option == 2:
                print("Please enter the details you want to edit:")
                modify = input()
                print("Please enter the new information:")
                new_information = input()
                print("Please enter the old information")
                old_information = input()

                update_book = f"""
                UPDATE
                    books
                SET
                    {modify} = '{new_information}'
                WHERE
                    {modify} = '{old_information}'
                """

                execute_query(connection, update_book)


            if option == 3:
                select_books = "SELECT * from book"
                books = execute_read_query(connection, select_books)
                for library in books:
                    print(library)


            if option == 4:
                print("Please enter the details of the book you want to delete")
                title = input("title \n> ")
                author = input("author\n>")
                delete_books = f"""
                DELETE
                    customer
                WHERE
                    title = '{title}'
                    first_name = '{author}'
                """
                execute_query(connection,delete_books)
                print(f"{title} was deleted")





