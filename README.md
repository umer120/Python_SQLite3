# Python_SQLite3
In this repository, I have uploaded a file which uses sqlite3 library to create CRUD Application

- This Python script demonstrates a basic CRUD (Create, Read, Update, Delete) application using SQLite for storing and managing user data. It allows you to insert, view, update, and delete records from a local database file called users_list.db.

- Connects to a SQLite database named users_list.db.

- If the file doesn't exist, it will be created automatically.

- A cursor object is created, which allows us to execute SQL commands.

- Creates a table named users with three fields: id, name, and age.

- id is an auto-incremented primary key, ensuring uniqueness for each record.

- Name must be provided (NOT NULL), while age is optional.

- A loop runs continuously to prompt the user for an operation until they choose to quit.

**_Option 1: Insert Data_**

- Takes name and age from the user.

- Inserts the data into the users table.

- Retrieves and prints all records from the users table.

**_Option 2: Read Data_** Retrieves and prints all records from the users table.

 
