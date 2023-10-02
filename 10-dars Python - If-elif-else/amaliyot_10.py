# Mavzu: If-Elif-Else
# Sana: 10/1/2023
# Muallif: Abbos

# j_son = float(input("Iltimos juft son kiriting>>>"))

# if j_son%2:
#     print("Bu son juft emas")
# else:
#     print("Rahmat!")

# f_yosh = int(input("Yoshingiz nechida?\n>>>"))

# if f_yosh<=4 or f_yosh<=60:
#     print("Sizga kirish bepul.")
# elif f_yosh<=18:
#     print("Sizga kirish 10000")
# else:
#     print("Sizga kirish 20000")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))

# if son1<=son2:
#     print(f"{son1}<{son2}")
# elif son1>=son2:
#     print(f"{son1}>{son2}")
# else:
#     print(f"{son1}={son2}")

# mahsulotlar = ['uzum', 'olma', 'gosht', 'kartoshka', 'piyoz', 'banan', 'anor', 'kalbasa', 'yog', 'kitob']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shish: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# foydalanuvchilar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# login = input("Login kiriting: ")

# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang")
# else:
#     print(f"Xush kelibsiz, {login}")

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%2):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")