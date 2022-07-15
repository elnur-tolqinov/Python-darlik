#mal'umot turi List (ro'yxat) deb ataladi. Ro'yxat o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash 
#imkonini beradi. Bu qiymatlar List elementlari deyiladi. Ro'yxatda son, matn yoki aralash turdagi elementlarni saqlash mumkin
 
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

#Ro'yxatdagi har bir element tartib bilan joylashgani sababli, biz istalgan elementga uning tartib raqami (indeksi) 
#bo'yicha murojat qilinadi. 
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
#Natija: Birinchi meva: olma  Ikkinchi meva: anjir

#Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llash mumkin
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())
#Natija: Birinchi meva: Olma , Ikkinchi meva: ANJIR

#List elementlari ustida arifmetik amallar bajarish:
narhlar = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])
#Natija: 32900

#Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin. Bu usul Listning 
#uzunligini bilmaganda juda kerak bo'ladi.
car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 
#Natija: Volkswagen

#listga malumotni o'zgartirish
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)
#Natija: [13000, 18000, 11000, 24000]

#listga yangi element qo'shish
#Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida ro'yxatning oxiriga qiymat qo'shish:
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shaladi
print(mevalar)
#Natija: ['olma', 'anjir', 'shaftoli', "o'rik", 'tarvuz']

cars = [] # bo'sh ro'yxat
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
print(cars)
#Natija: ['Lacetti', 'Nexia 3', 'Cobalt']

#Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. .insert() metodi ichida
#yangi elementning indeksi va qiymati beriladi:
cars = ['Lacetti', 'Nexia 3', 'Cobalt']
cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shadi
print(cars)
#Natija: ['Malibu', 'Lacetti', 'Nexia 3', 'Cobalt']

cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
print(cars)
#Natija: ['Malibu', 'Lacetti', 'Damas', 'Nexia 3', 'Cobalt']

#Listdan malumot o'chirish
#Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
del mevalar[1] # 2-element (anjir) ni o'chirib tashlaydi
print(mevalar)
#Natija: ['olma', 'shaftoli', "o'rik", 'anor']

#Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. Buning uchun qavs 
#ichida o'chirib tashlash kerak bo'lgan qiymatni yoziladi
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
print(mevalar)
#Natija: ['olma', 'anjir', "o'rik", 'anor']

#.remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning 
#ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
print(hayvonlar)
#Natija: ['it', 'sigir', "qo'y", 'quyon', 'mushuk']

#Listdan element sug'urub olish
#Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va 
#undan foydalanish talab qilinishi mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalaniladi.
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)
#Natija: 
# Men banan sotib oldim 
# Olinmagan mahsulotlar: ["yog'", 'un', 'piyoz', "go'sht"]

#Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.