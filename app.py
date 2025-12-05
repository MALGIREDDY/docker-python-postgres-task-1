import psycopg2
import time

# Wait for Postgres to start
time.sleep(5)

try:
    conn = psycopg2.connect(
        host="postgres",
        database="mydb",
        user="user",
        password="pass"
    )

    print("Connected to PostgreSQL!")

    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)

    # Insert one row
    cur.execute("INSERT INTO students (name) VALUES ('Saideep') RETURNING id;")
    new_id = cur.fetchone()[0]
    conn.commit()

    print(f"Inserted row with ID: {new_id}")

    # Fetch rows
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()

    # Box-style output
    print("\n+----+----------------+")
    print("| ID | NAME           |")
    print("+----+----------------+")
    for row in rows:
        print(f"| {row[0]:<2} | {row[1]:<14} |")
    print("+----+----------------+\n")

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
