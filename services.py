# username va parol

def signup(username, password):
    f = open("users.txt", "a")
    f.write(f"{username} {password}\n")
    f.close()

def login(username, password):
    f = open("users.txt", "r")
    isTrue = False
    for line in f:
        if line == f"{username} {password}\n":
            isTrue = True
            break

    return isTrue
