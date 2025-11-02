from data import Orang

def login(username, password, role_input):
    if username in Orang and Orang[username]["password"] == password:
        if Orang[username]["role"] == role_input:
            return True
    return False

def registrasi(username_baru, password_baru):
    if username_baru in Orang:
        return False
    Orang[username_baru] = {"password": password_baru, "role": "member"}
    return True