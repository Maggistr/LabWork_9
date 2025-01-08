class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password


user = UserAccount("user123", "user@example.com", "securepassword")
print("Пароль корректен:", user.check_password("securepassword"))
user.set_password("newsecurepassword")
print("Пароль корректен:", user.check_password("newsecurepassword"))
print("Пароль корректен:", user.check_password("securepassword"))
