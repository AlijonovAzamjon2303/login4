import services
menu = """
1. Ro'yxatdan o'tish
2. Kirish
"""
while True:
    print(menu)
    choice = input(">>> ")
    if choice == "1":
        username = input("Username : ")
        password = input("Password : ")
        services.signup(username, password)
        print(f"{username} muvaffaqiyatli ro'yxatdan o'tdingiz!")
    elif choice == "2":
        username = input("Username : ")
        password = input("Password : ")
        if services.login(username, password):
            print(f"{username} xush kelibsiz!")
        else:
            print("Siz avval ro'yxatdan o'tishingiz kerak!")