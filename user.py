# user.py
from database import connect_db
from user_base import User

class RegularUser(User):
    def place_order(self, user_id, menu_item):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (user_id, menu_item, status) VALUES (?, ?, ?)", (user_id, menu_item, 'pending'))
        conn.commit()
        conn.close()

    def view_user_orders(self, user_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        orders = cursor.fetchall()
        conn.close()
        return orders

    def view_menu(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM menu")
        menu = cursor.fetchall()
        conn.close()
        return menu
