# 3-dars: String (Matn)
# Sana: 9/17/2023
# Muallif: Abbos

# shahar = "Фаргона"
# viloyat = "кукон"

# matn = 'Men yangi 📱 oldim'
# print(matn)

# STRING USTIDA AMALLAR

# ism = "Ahmad"
# print("Mening ismim " + ism)

# ism = "Ahad"
# familiya = "Qayum"
# print(ism + familiya)

# ism = "Ahad"
# familiya = "Qayum"
# print(ism + ' ' + familiya)

# f-STRING

# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# MAHSUS BELGILAR

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')

# STRING METODLAR

# ism = 'james'
# familiya = 'bond'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva = "    olma     "
# print(meva)
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# INPUT

# ism = input("Ismingiz nima? ")
# print("Assalomu aleykum, " + ism)

ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi.
print("Assalom aleykum, " + ism.title())