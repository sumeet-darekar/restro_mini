# staff.py
from database import connect_db
from user_base import Staff

class StaffUser(Staff):
    def view_orders(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        conn.close()
        return orders

    def update_order_status(self, order_id, status):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
        conn.commit()
        conn.close()
