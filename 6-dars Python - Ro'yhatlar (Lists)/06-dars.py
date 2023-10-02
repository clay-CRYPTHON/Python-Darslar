# 3-dars: Lists (Ro'yhatlar)
# Sana: 9/21/2023
# Muallif: Abbos

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narhlar =[12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
# sonlar = ['bir', 'ikki', 3, 4, 5]
# ismlar = []

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# .append()

# mevalar = ['olma', 'anjir', 'shoftoli', "o'rik"]
# mevalar.append("tarvuz") # mebvlarga tarvuz qo'shamiz
# print(mevalar)

# cars = [] # Bo'sh ro'yhat taratamiz
# cars.append('Lacetti') # Ro'yhatga Lacettini qo'shamiz
# cars.append('Nexia 3') # Ro'yhatga Nexia 3 ni qo'shamiz
# cars.append('Cobalt')  # Ro'yhatga Cobalt ni qo'shamiz
# print(cars)

# .insert

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu')
# print(cars)
# cars.insert(2, 'Damas')
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar [1]
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)

# bozorlik = ['yog\'', 'un', 'piyoz', 'banan', 'go\'sht']
# mahsulot = bozorlik.pop(3)
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)