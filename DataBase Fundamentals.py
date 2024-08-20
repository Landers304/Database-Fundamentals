#Task 1:



import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('BookHaven.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the Authors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        bio TEXT
    )
''')

# Create the Books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        publication_year INTEGER,
        price REAL CHECK (price >= 0),
        stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0),
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    )
''')

# Create the Customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone_number TEXT,
        address TEXT
    )
''')

# Create the Transactions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        book_id INTEGER,
        transaction_date TEXT NOT NULL,
        quantity INTEGER NOT NULL CHECK (quantity > 0),
        total_amount REAL NOT NULL CHECK (total_amount >= 0),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
''')

# Commit the changes and close the connection
connection.commit()
connection.close()