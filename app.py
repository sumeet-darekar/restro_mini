# app.py
import streamlit as st
from admin import AdminUser
from staff import StaffUser
from user import RegularUser  # Ensure this line is present
from database import create_tables


def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    role = st.sidebar.selectbox("Role", ["user", "staff", "admin"])
    
    if st.sidebar.button("Login"):
        # Here, you should validate the user login using the database
        st.session_state["role"] = role
        st.session_state["username"] = username
        return True
    return False

def admin_panel(user):
    st.title("Admin Panel")
    if st.checkbox("Add Staff"):
        username = st.text_input("Staff Username")
        password = st.text_input("Staff Password")
        if st.button("Add Staff"):
            user.add_staff(username, password)
            st.success("Staff added successfully!")
    
    if st.checkbox("Delete Staff"):
        staff_id = st.number_input("Staff ID", step=1)
        if st.button("Delete Staff"):
            user.delete_staff(staff_id)
            st.success("Staff deleted successfully!")

    if st.checkbox("Add Menu Item"):
        item_name = st.text_input("Menu Item Name")
        price = st.number_input("Price")
        if st.button("Add Menu"):
            user.add_menu_item(item_name, price)
            st.success("Menu item added!")

    if st.checkbox("Delete Menu Item"):
        item_id = st.number_input("Menu Item ID", step=1)
        if st.button("Delete Menu"):
            user.delete_menu_item(item_id)
            st.success("Menu item deleted!")

def staff_panel(user):
    st.title("Staff Panel")
    orders = user.view_orders()
    for order in orders:
        st.write(f"Order ID: {order[0]}, Menu Item: {order[2]}, Status: {order[3]}")
        if st.button(f"Mark Completed {order[0]}"):
            user.update_order_status(order[0], "completed")
            st.success(f"Order {order[0]} marked as completed")

def user_panel(user):
    st.title("User Panel")
    menu = user.view_menu()
    for item in menu:
        st.write(f"Item: {item[1]}, Price: {item[2]}")
    
    selected_item = st.selectbox("Select Item to Order", [item[1] for item in menu])
    
    if st.button("Place Order"):
        # Here, you should capture the user_id dynamically
        user.place_order(user_id=1, menu_item=selected_item)
        st.success(f"Order placed for {selected_item}")

def main():
    st.title("Dummies Restro & Bar")
    create_tables()
    
    if "role" not in st.session_state:
        if not login():
            return

    role = st.session_state.get("role")
    
    if role == "admin":
        admin_user = AdminUser()
        admin_panel(admin_user)
    elif role == "staff":
        staff_user = StaffUser()
        staff_panel(staff_user)
    else:
        regular_user = RegularUser()
        user_panel(regular_user)

if __name__ == "__main__":
    main()
