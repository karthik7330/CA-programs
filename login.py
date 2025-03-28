hdef login(username, password):
    # A simple hardcoded check for demonstration purposes
    if username == "admin" and password == "password":
        return "Login successful"
    else:
        return "Login failed"
