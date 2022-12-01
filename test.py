fichier = open("passwords.txt", "r", encoding="utf-8")
file = open("password.txt", "a", encoding="utf-8")
list = []
for i in fichier:
    if i not in list:
        list.append(i)
        file.write(i)

    else :
        continue
file.close()