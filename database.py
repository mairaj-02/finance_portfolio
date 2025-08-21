import os
from cs50 import SQL

def initialize_database():
    # Check if database file exists
    db_exists = os.path.exists("finance.db")
    
    # Configure CS50 Library to use SQLite database
    db = SQL("sqlite:///finance.db")
    
    if not db_exists:
        # Create the database file and users table
        db.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username TEXT NOT NULL,
                hash TEXT NOT NULL,
                cash NUMERIC NOT NULL DEFAULT 10000.00
            )
        """)
        
        # Create unique index on username
        db.execute("CREATE UNIQUE INDEX username ON users (username)")
    
    # Check if transactions table exists
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='transactions'")
    
    if not tables:
        # Create transactions table
        db.execute("""
            CREATE TABLE transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_id INTEGER NOT NULL,
                symbol TEXT NOT NULL,
                shares INTEGER NOT NULL,
                price NUMERIC NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
    
    return db