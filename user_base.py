# user_base.py
class User:
    def __init__(self):
        self.role = None

    def display_info(self):
        return f"Role: {self.role}"

class Staff(User):
    def __init__(self):
        super().__init__()
        self.role = "Staff"

class Admin(User):
    def __init__(self):
        super().__init__()
        self.role = "Admin"
