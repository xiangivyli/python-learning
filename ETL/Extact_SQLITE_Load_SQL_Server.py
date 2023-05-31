import sqlite3
import pyodbc

# Step 1: Extract tables and columns from SQLite

# Connect to the SQLite database file
conn = sqlite3.connect('D:/Learn_DS/Git/python-learning/ETL/data/database.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Retrieve the table names from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()

# Dictionary to store table data
table_data = {}

# Iterate over each table
for table_name in table_names:
    table_name = table_name[0]  # Extract the table name from the result tuple
    
    # Execute the PRAGMA statement to get column information
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()

    # Extract the column names and datatypes
    column_names = [column[1] for column in columns]
    column_datatypes = [column[2] for column in columns]

    # Store the column names and datatypes in the dictionary
    table_data[table_name] = {
        'column_names': column_names,
        'column_datatypes': column_datatypes
    }


# Step 2: Connect to SQL Server

# Establish a connection to SQL Server
conn_sqlserver = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-FIS40MH\MSSQLSERVER01;"
    "DATABASE_NAME=Project;"
    "Trusted_Connection=yes;"
)

# Create a cursor object for SQL Server
cursor_sqlserver = conn_sqlserver.cursor()

# Step 3: Create tables and insert data into SQL Server

# Iterate over each table
for table_name, table_data in table_data.items():
    # Extract column names and datatypes
    column_names = table_data['column_names']
    column_datatypes = table_data['column_datatypes']
    
    # Create the table in SQL Server
    create_table_query = f"CREATE TABLE {table_name} ("
    create_table_query += ', '.join([f"{column_name} {column_datatype}" for column_name, column_datatype in zip(column_names, column_datatypes)])
    create_table_query += ")"
    
    cursor_sqlserver.execute(create_table_query)

    # Insert data into the table
    insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(column_names))})"
    data_rows = cursor.execute(f"SELECT * FROM {table_name}").fetchall()

    cursor_sqlserver.executemany(insert_query, data_rows)

# Step 4: Commit and close connections

# Close the SQLite connection
conn.close()

# Commit and close SQL Server connection
conn_sqlserver.commit()
conn_sqlserver.close()
