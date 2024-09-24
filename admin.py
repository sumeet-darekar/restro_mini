from database import connect_db

def add_staff(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, 'staff'))
    conn.commit()
    conn.close()

def delete_staff(staff_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (staff_id,))
    conn.commit()
    conn.close()

def add_menu_item(item_name, price):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO menu (item_name, price) VALUES (?, ?)", (item_name, price))
    conn.commit()
    conn.close()

def delete_menu_item(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menu WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
