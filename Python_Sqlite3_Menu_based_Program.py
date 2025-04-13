import sqlite3
   
def main():
    conn=sqlite3.connect("users_list.db")
    cursor=conn.cursor()
        
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           age INTEGER
             )
        """)
        
    conn.commit()
    while(True):
        print("Select the operation you want to perform (Insert,Read,Update,Delete,Quit): ")
        print("1: Insert the data in the table")
        print("2: Read the data in the table")
        print("3: Update the existing data in the table")
        print("4: Delete the data from the table")
        print("5: Quit")
        option = int(input("Option: "))
        if option == 1:
            Name = input("Input name ? ")
            Age = int(input("Input age ? "))
            cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",(Name,Age))
            conn.commit()
            print("Inserted Successfully..!!!")
        elif option == 2:
            cursor.execute("SELECT * FROM users")
            rows=cursor.fetchall()
            print("\nUsers are as follows:")
            for row in rows:
                print(row) 
        elif option == 3:
            prim_id = int(input("Enter id ? "))
            val1 = input("What you want to update ? (name,age,both)")
            if val1 == "name":
                value = input("Enter name :")
                cursor.execute("UPDATE users SET name = ? WHERE id = ?",(value,prim_id))
                conn.commit()
                print("Name updated successfully...!!")
            elif val1 == "age":
                value = int(input("Enter age :"))
                cursor.execute("UPDATE users SET age = ? WHERE id = ?",(value,prim_id))
                conn.commit()
                print("Age updated successfullly...!!")
            elif val1 == "both":
                value1 = input("Enter name :")
                value2 = int(input("Enter age :"))
                cursor.execute("UPDATE users SET name = ? , age = ? WHERE id = ?",(value1,value2,prim_id))
                conn.commit()
                print("Both name and ages updated successfully..!!")
            else:
                print("WRONG INPUT!!!")
        elif option == 4:
            prim_id = int(input("Enter id ? "))
            cursor.execute("DELETE FROM users WHERE id = ?",(prim_id,))
            conn.commit()
            print("User deleted Successfully!!")
        elif option == 5:
            print("Thank You!!")
            break

main()

    
