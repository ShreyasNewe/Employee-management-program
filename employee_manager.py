import streamlit as st
import psycopg2
from datetime import date

# Configurable table name
TABLE_NAME = "employeee"  # 🔁 Replace with your actual table name

# DB Connection
def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="CompanyDB",
        user="postgres",
        password="your_password_here",  # 🔒 Replace with your actual password
        port=5432  # 🔁 Replace if you're using a custom port
    )

# DB Functions
def insert_employee(conn, fname, lname, title, dept, salary, doj):
    with conn.cursor() as cur:
        cur.execute(f"""
            INSERT INTO {TABLE_NAME} (fname, lname, title, dept, salary, DOJ)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (fname, lname, title, dept, salary, doj))
    conn.commit()

def fetch_employees(conn):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY id;")
        return cur.fetchall()

def fetch_employee_by_id(conn, emp_id):
    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = %s;", (emp_id,))
        return cur.fetchone()

def update_employee(conn, emp_id, fname, lname, title, dept, salary, doj):
    with conn.cursor() as cur:
        cur.execute(f"""
            UPDATE {TABLE_NAME}
            SET fname=%s, lname=%s, title=%s, dept=%s, salary=%s, DOJ=%s
            WHERE id=%s;
        """, (fname, lname, title, dept, salary, doj, emp_id))
    conn.commit()

def delete_employee(conn, emp_id):
    with conn.cursor() as cur:
        cur.execute(f"DELETE FROM {TABLE_NAME} WHERE id = %s;", (emp_id,))
    conn.commit()

# Streamlit UI Configuration
st.set_page_config(page_title="Employee Manager", layout="centered")
st.title("Employee Manager")
menu = st.sidebar.selectbox("Menu", ["Add", "View", "Update", "Delete"])

# DB connection
conn =
