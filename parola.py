import random 

semboller = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Kaç haneli şifre üreteyim?"))

parola = ""
for i in range(uzunluk):
    parola += random.choice(semboller)

print(parola)