fichier = open("passwords.txt", "r", encoding="utf-8")

list = []
for i in fichier:
    if i not in list:
        list.append(i)

    else :
        continue

file = open("password.txt", "a", encoding="utf-8")
for j in list:
    file.write("\n".j)
file.close()