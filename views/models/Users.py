class Users:
    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def login(self, input_email, input_password):
        if self.email == input_email and self.password == input_password:
            return True, f"Login successful! Role: {self.role}"
        else:
            return False, "Invalid credentials"

    def check_role(self):
        return self.role
