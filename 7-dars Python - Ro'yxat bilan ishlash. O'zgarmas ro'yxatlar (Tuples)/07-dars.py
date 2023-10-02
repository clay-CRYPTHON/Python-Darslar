# Mavzu: Ro'yhat bilan ishlash. O'zgarmas ro'yhatlar (Tuples)
# Sana: 9/21/2023
# Muallif: Abbos

# # TARTIBLASH
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# # KATTA VA KICHIK HARF
# cars = ['Bmw', 'merecdes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# # TESKARI TARTIB
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# # SORTED()
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yhat:", sorted(mehmonlar))
# print("Asl ro'yhat o'zgarmas qoldi:", mehmonlar)
# print(sorted(mehmonlar, reverse=True))

# # SONLI RO'YHATLAR
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# # RO'YHATNI ORTIDAN BOSHLAB CHIQARISH
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'Lemon']
# fruits.reverse()
# print(fruits)

# # RO'YHAT UZUNLIGI
# fruits = ['pear', 'banana', 'apple', 'watermelan', 'Lemon']
# print("Elementlar soni:", len(fruits)) # Len(fruits) ro'yhatlar uzunligini qaytaradi

# # RANGE
# sonlar = list(range(0,10))
# print(sonlar)

# # RANGE VA QADAM
# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# # MIN(), MAX(), SUM()
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh", arzon, ". Eng qimmati", qimmat, ". Jami:", jami)

# # RO'YHATNI KESISH
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3]
# print(my_cars)
# print(cars[2:5])
# print(cars[:4])
# print(cars[2:])

# # ROYHATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yhati:", sonlar)
# print("Bu sonlar2 ro'yhati", sonlar2)

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yhati:", sonlar2)
# print("Bu sonlar2 ro'yhati:", sonlar2)

# # TUPLES
# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# toys[3] = 'dragon'

# # TUPLES<->LIST
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# toys = list(toys)
# # RO'YHATGA O'ZGARTIRISHLAR KIRITAMIZ
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'macqueen'
# toys =  tuple(toys)
# print(toys)