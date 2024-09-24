# user.py
from database import connect_db

def view_menu():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu")
    menu = cursor.fetchall()
    conn.close()
    return menu

def place_order(user_id, menu_item):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (user_id, menu_item, status) VALUES (?, ?, ?)", (user_id, menu_item, 'pending'))
    conn.commit()
    conn.close()

def view_user_orders(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
    orders = cursor.fetchall()
    conn.close()
    return orders
