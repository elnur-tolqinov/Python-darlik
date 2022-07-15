#Listni yani ro'yhatni tartiblash
#Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun 
#list uchun maxsus .sort() metodidan foydalaniladi.
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)
#Natija: ['audi', 'bmw', 'general motors', 'mercedes benz', 'tesla', 'volvo'] 
#yuqoridagi ro'yxat alifbo bo'yicha tartiblandi.

cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
cars.sort()
print(cars)
#Natija: ['Bmw', 'audi', 'gm', 'mercedes benz', 'tesla', 'volvo']
#Yuqoridagi misolda 'Bmw' elementi katta harf bilan boshlangani uchun ro'yxatning boshidan joy oldi.

#Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz. 
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)
#Natija: ['volvo', 'tesla', 'mercedes benz', 'general motors', 'bmw', 'audi']

#.sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini 
#buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
#Natija: 
# sorted() qaytargan ro'yxat: ['Avazbek', 'Farruh', 'Hamid', 'Odil', 'Shamsiddin', 'Temur'] 
# Asl ro'yxat o'zgarmas qoldi: ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']

#sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
print(sorted(mehmonlar, reverse=True))
#Natija: ['Temur', 'Shamsiddin', 'Odil', 'Hamid', 'Farruh', 'Avazbek']

#Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))
#Natija:
#[11, 12, 34, 34, 65, 76, 98]
#[98, 76, 65, 34, 34, 12, 11]

#Listni aylantirish
#Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning 
#uchun .reverse() metodidan foydalanamiz.
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)
#Natija: ['lemon', 'watermelon', 'apple', 'banana', 'pear']
#Natija va asl ro'yxatni solishtiring.

#Listni ro'yhatni uzunligin bilish
#Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi
#Natija: Elementlar soni: 5

#range()Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list()
#funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
sonlar = list(range(0,10))
print(sonlar)
#Natija: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Yuqoridagi misolda range(0,10) funktsiyasi 0 dan 9 gacha sonlar ketma-ketligini shakllantirdi, 
#list(range(0,9)) esa bu ketma-ketlikni ro'yxatga aylantirdi.

#range() yordamida qadamni ham berishimiz mumkin:
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)
#Natija:
#Juft sonlar: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] 
#Toq sonlar: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#o'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni topish uchun 
#esa max() funktsiyasidan, sonlarning yig'indisini topish uchun esa sum() funktsyasidan foydalansak bo'ladi:
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
#Natija: Eng arzon narh 5600 . Eng qimmati 32874 . Jami: 116164

#Ro'yhatni kesish
#ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin, deylik biz quyidagi cars degan 
#ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz, buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars) 
#Natija: ['bmw', 'mercedes benz', 'volvo']

#Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi. Agar 2-indeksni 
#kiritmasangiz, ro'yxat oxirigacha kesadi:
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
#Natija:
# ['bmw', 'mercedes benz', 'volvo', 'general motors'] 
#['volvo', 'general motors', 'tesla', 'audi']

#Ro'yhatdan nusxa olish
sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)
#Natija:Bu sonlar ro'yxati: [1, 2, 3, 4, 5]
#Bu sonlar2 ro'yxati: [1, 2, 3, 4, 5, 6, 7]

#TUPLES O'ZGARMAS RO'YHAT
#Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin. Pythonda bunday ro'yxatlar tuples
#deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. 
#List dan farqli ravishda, Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:

#Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi:
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
#Natija:
# bus 
# lizard 
# ('bear', 'dino', 'snake')

#Tuple ichidagi biror elementning qiymatini o'zgartirib ko'ramiz:
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
#Natija: ('car', 'mcqueen', 'dino', 'snake', 'lizard', 'dragon')
