 🚀 Dockerized Python + PostgreSQL Mini Project

This project demonstrates how to run a **Python application** and a **PostgreSQL database** together using **Docker**, **Docker Compose**, and a **custom network**.

The Python app:

- Connects to PostgreSQL  
- Creates a table  
- Inserts one row  
- Reads and displays the row  
- Prints the output in a clean box-style table  

This project is created as part of a **beginner DevOps mini task**.

---

## 📂 Project Structure

docker-python-postgres-task/
│── app.py
│── Dockerfile
│── requirements.txt
└── docker-compose.yml

python
Copy code

---

## 🧠 How It Works (Architecture)

Docker Compose runs two containers:

1. **PostgreSQL container**  
2. **Python application container**

Both containers communicate through a custom Docker network named `mynetwork`.

The workflow:

1. PostgreSQL starts  
2. Python waits 5 seconds  
3. Connects to PostgreSQL  
4. Creates table  
5. Inserts one row  
6. Reads & prints data using a formatted table  

---

## 🐍 app.py (Python Application)

```python
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

    # Insert a row
    cur.execute("INSERT INTO students (name) VALUES ('Saideep') RETURNING id;")
    new_id = cur.fetchone()[0]
    conn.commit()

    print(f"Inserted row with ID: {new_id}")

    # Fetch all rows
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
📦 Dockerfile
dockerfile
Copy code
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
📜 requirements.txt
php
Copy code
psycopg2-binary
🧱 docker-compose.yml
yaml
Copy code
services:
  postgres:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    networks:
      - mynetwork

  python_app:
    build: .
    depends_on:
      - postgres
    networks:
      - mynetwork

networks:
  mynetwork:
▶️ How to Run the Project
Step 1 — Open terminal in project folder
bash
Copy code
cd docker-python-postgres-task
Step 2 — Run using Docker Compose
css
Copy code
docker compose up --build
🎉 Expected Output
pgsql
Copy code
Connected to PostgreSQL!
Inserted row with ID: 1

+----+----------------+
| ID | NAME           |
+----+----------------+
| 1  | Saideep        |
+----+----------------+
You may see multiple rows if you run the container multiple times.

🐳 Docker Desktop Logs (Optional)
You can view output in:

Docker Desktop → Containers → python_app → Logs

🔄 Reset the Database (Start Fresh)
To remove all database data:

nginx
Copy code
docker compose down -v
This deletes volumes so PostgreSQL restarts clean.

✔️ This Project Covers
Dockerfile

Python + PostgreSQL integration

Custom Docker network

Using psycopg2

Docker Compose multi-container orchestration

Table formatting in Python

📘 Author
Saideep
Beginner DevOps Engineer