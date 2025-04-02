import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1l0v3luffy',  # Use your actual password here
    database='mydatabase'     # Use your actual database name here
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# SQL query to create a new table
def create_table_query():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS yourtable (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    )
    """

    return create_table_query




def create_insert_query():
    insert_query = "INSERT INTO yourtable (name, age) VALUES (%s, %s)"
    values = input("Enter values for name and age separated by a comma: ").split(",")
    values = [value.strip() for value in values]  # Clean up the input
    return insert_query,values




# Commit the transaction to save changes



def get_select_query():
    select_query = "SELECT * FROM yourtable"
    cursor.execute(select_query)  # Execute the query first
    rows = cursor.fetchall()  # Fetch all results
    
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    else:
        print("No data found.")







if __name__ == "__main__":
    
    def menu ():
        while True:
            print("1. Create Table")
            print("2. Insert Data")
            print("3. Select Data")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                cursor.execute(create_table_query())
                conn.commit()
                print("Table created successfully!")
            elif choice == '2':
                insert_query, values = create_insert_query()
                cursor.execute(insert_query, values)
                conn.commit()
                print("Data inserted successfully!")
            elif choice == '3':
                get_select_query()
                
            else: 
                print("Exiting...")
                cursor.close()
                conn.close()
                exit()

menu()
