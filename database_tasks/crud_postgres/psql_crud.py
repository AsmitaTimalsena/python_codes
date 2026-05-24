import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="1234",
    host="localhost",
    port="5432",
    database="asmidb",
)

print(conn)
print("Connection successful")


def create_table():
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INT NOT NULL
                );
                """
            )
            print("Table created successfully")


create_table()


def insert_user():
    cur = conn.cursor()
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cur.execute(
        """
        INSERT INTO students (name, age)
        VALUES (%s, %s);
        """,
        (name, age),
    )
    conn.commit()
    cur.close()


def fetch_users():
    cur = conn.cursor()
    print("Fetching students...")
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()


def update_user():
    cur = conn.cursor()
    user_id = int(input("Enter user id to update: "))
    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))
    cur.execute(
        """
        UPDATE students
        SET name = %s, age = %s
        WHERE id = %s;
        """,
        (new_name, new_age, user_id),
    )
    conn.commit()
    cur.close()


def delete_user():
    cur = conn.cursor()
    name = input("Enter name to delete: ")
    cur.execute(
        """
        DELETE FROM students
        WHERE name = %s;
        """,
        (name,),
    )
    conn.commit()
    cur.close()

while True:
    print("-----------------STUDENT MANAGEMENT-----------------")
    print("Choose an option(1-5):")
    print("1. Insert Student")
    print("2. Fetch Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_user()
    elif choice == "2":
        fetch_users()
    elif choice == "3":
        update_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
conn.close()

