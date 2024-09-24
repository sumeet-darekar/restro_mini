
import streamlit as st
from admin import add_staff, delete_staff, add_menu_item, delete_menu_item
from staff import view_orders, update_order_status
from user import view_menu, place_order, view_user_orders
from database import create_tables

def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    role = st.sidebar.selectbox("Role", ["user", "staff", "admin"])
    if st.sidebar.button("Login"):
        # Here, validate the user login using the database (can be added)
        st.session_state["role"] = role
        st.session_state["username"] = username
        return True
    return False

def admin_panel():
    st.title("Admin Panel")
    if st.checkbox("Add Staff"):
        username = st.text_input("Staff Username")
        password = st.text_input("Staff Password")
        if st.button("Add Staff"):
            add_staff(username, password)
            st.success("Staff added successfully!")
    
    if st.checkbox("Delete Staff"):
        staff_id = st.number_input("Staff ID", step=1)
        if st.button("Delete Staff"):
            delete_staff(staff_id)
            st.success("Staff deleted successfully!")

    if st.checkbox("Add Menu Item"):
        item_name = st.text_input("Menu Item Name")
        price = st.number_input("Price")
        if st.button("Add Menu"):
            add_menu_item(item_name, price)
            st.success("Menu item added!")

    if st.checkbox("Delete Menu Item"):
        item_id = st.number_input("Menu Item ID", step=1)
        if st.button("Delete Menu"):
            delete_menu_item(item_id)
            st.success("Menu item deleted!")

def staff_panel():
    st.title("Staff Panel")
    orders = view_orders()
    for order in orders:
        st.write(f"Order ID: {order[0]}, Menu Item: {order[2]}, Status: {order[3]}")
        if st.button(f"Mark Completed {order[0]}"):
            update_order_status(order[0], "completed")
            st.success(f"Order {order[0]} marked as completed")

def user_panel():
    st.title("User Panel")
    menu = view_menu()
    for item in menu:
        st.write(f"Item: {item[1]}, Price: {item[2]}")
    selected_item = st.selectbox("Select Item to Order", [item[1] for item in menu])
    if st.button("Place Order"):
        # Here, you should capture the user_id
        place_order(user_id=1, menu_item=selected_item)
        st.success(f"Order placed for {selected_item}")

def main():
    st.title("Hotel Management System")
    create_tables()
    
    if "role" not in st.session_state:
        if not login():
            return

    role = st.session_state.get("role")
    if role == "admin":
        admin_panel()
    elif role == "staff":
        staff_panel()
    else:
        user_panel()
def user_panel():
    st.title("User Panel")

    # Fetch user ID (for now, we assume user_id = 1 for the demo; this should be dynamic in a real app)
    user_id = 1  # Change this to the actual logged-in user's ID

    # View Menu and Place Order
    st.header("Menu")
    menu = view_menu()
    for item in menu:
        st.write(f"Item: {item[1]}, Price: {item[2]}")
    
    selected_item = st.selectbox("Select Item to Order", [item[1] for item in menu])
    
    if st.button("Place Order"):
        place_order(user_id, selected_item)
        st.success(f"Order placed for {selected_item}")

    # Display User's Orders
    st.header("Your Orders")
    orders = view_user_orders(user_id)
    
    if orders:
        for order in orders:
            st.write(f"Order ID: {order[0]}, Menu Item: {order[2]}, Status: {order[3]}")
    else:
        st.info("You have not placed any orders yet.")


if __name__ == "__main__":
    main()
