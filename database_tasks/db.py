
import psycopg2


class Database:
    def __init__(self):
        print("\n Initializing Database Setup...")

        self.db_name = "asmidb"
        self.user = "postgres"
        self.password = ""
        self.host = "localhost"
        self.port = "5432"


        # Step 1: Check/Create Database
        self.create_database_if_not_exists()

        # Step 2: Connect to Database
        self.connect()

        # Step 3: Create Table
        self.create_table()

    def create_database_if_not_exists(self):
        print("\nStep 1: Checking database...")
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                (self.db_name,)
            )
            exists = cursor.fetchone()

            if exists:
                print(f"Database '{self.db_name}' already exists")
            else:
            
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(
                        sql.Identifier(self.db_name)
                    )
                )
                print(f"Database '{self.db_name}' created successfully")

            cursor.close()
            conn.close()

        except Exception as e:
            print("Error while checking/creating database:", e)

    # Step 2: Connect
    def connect(self):
        print("\n Step 2: Establishing connection...")

        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.conn.cursor()

            print(f"Connected to database '{self.db_name}' successfully")

        except Exception as e:
            print(" Connection failed:", e)

    #  Step 3: Create table
    def create_table(self):
        print("\n Step 3: Checking/Creating table...")

        try:
            query = """
            CREATE TABLE IF NOT EXISTS students (
                roll_no SERIAL PRIMARY KEY,
                name VARCHAR(100),
                dob DATE,
                education VARCHAR(100),
                address TEXT
            );
            """
            self.cursor.execute(query)
            self.conn.commit()

            print(" Table 'students' is ready")

        except Exception as e:
            print(" Error creating table:", e)

    
    #  INSERT
    def insert_student(self, name, dob, education, address):
        print("\n Inserting student...")

        try:
            query = """
            INSERT INTO students (name, dob, education, address)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (name, dob, education, address)) 
            self.conn.commit()

            print(" Student added successfully")

        except Exception as e:
            print(" Insert error:", e)

    
        # SELECT
    def view_students(self):
        print("\n Fetching student data...")

        try:
            self.cursor.execute("SELECT * FROM students")
            data = self.cursor.fetchall()

            if not data:
                print("️ No records found")
            else:
                print(f" {len(data)} record(s) fetched")

            return data

        except Exception as e:
            print(" Fetch error:", e)
            return []
    
    def update_student(self, roll_no, name=None, dob=None, education=None, address=None):
        print("\n Updating student...")

        try:
            updates = []
            values = []

            if name is not None:
                updates.append("name = %s")
                values.append(name)

            if dob is not None:
                updates.append("dob = %s")
                values.append(dob)

            if education is not None:
                updates.append("education = %s")
                values.append(education)

            if address is not None:
                updates.append("address = %s")
                values.append(address)

            # If nothing to update
            if not updates:
                print(" No fields to update")
                return

            query = f"""
            UPDATE students
            SET {", ".join(updates)}
            WHERE roll_no = %s
            """

            values.append(roll_no)

            self.cursor.execute(query, tuple(values))
            self.conn.commit()

            print(" Student updated successfully")

        except Exception as e:
            print(" Update error:", e)
        
    
    def delete_student(self, roll_no):
        print("\n Deleting student...")

        try:
            query = "DELETE FROM students WHERE roll_no = %s"
            self.cursor.execute(query, (roll_no,))
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print(" No student found with given roll number")
            else:
                print(" Student deleted successfully")

        except Exception as e:
            print(" Delete error:", e)
    
        
    
    def close(self):
        print("\n Closing database connection...")

        try:
            self.cursor.close()
            self.conn.close()
            print("Connection closed successfully")

        except Exception as e:
            print("Error closing connection:", e)