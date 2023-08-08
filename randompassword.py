import random
char = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
length = int(input("enter length: "))
password = ""


for a in range(length):
    password += random.choice(char)
    print(password)
