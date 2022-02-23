class User:
    def __init__(self, first_name, last_name, username, email, login_count, last_login):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.last_login = last_login
        self.login_count = login_count

    def __str__(self):
        return str(vars(self))

    def to_dict(self):
        return vars(self)
