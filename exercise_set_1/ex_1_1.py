def get_username(email):
    if isinstance(email, str):
        if '@' in email:
            segments = email.split('@')
            username = segments[0]
            return username.lower()
        else:
            return None
    else:
        return None
