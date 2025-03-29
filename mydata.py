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
insert_query = "INSERT INTO yourtable (name, age) VALUES (%s, %s)"
values = ('Aaryn Minyard', 23)

cursor.execute(insert_query, values)
conn.commit()
print("Data inserted successfully!")


select_query = "SELECT * FROM yourtable"

# Execute the query
cursor.execute(select_query)

# Fetch all rows from the result
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Close the cursor and connection
cursor.close()
conn.close()
