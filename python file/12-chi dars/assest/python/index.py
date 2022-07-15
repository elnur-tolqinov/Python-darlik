 #SyntaxError-SINTEKS XATOLIK 
 #print "Hello World!"
#Natija:SyntaxError: deb beradi kodni bunday yoz debdi --> ("Hello World!")?

#EOL va EOF xatolik
#print("Hello World!
#Natija: SyntaxError: EOL while scanning string literal
#EOF (End of function - funktsiya yakuni) xatoligi esa funktsiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.  

#print("Hello World!"
#Natija: SyntaxError: unexpected EOF while parsing
#EOF xatoligining muammoli tarafi, Python aynan qaysi funktsiya yopilmay qolganini ko'rsata olmaydi, ya'ni
#kodni sinchiklab ko'zdan kechirib chiqish talab qilinadi.


#IndentationError - JOY TASHLASHDA XATOLIK
#print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)
#Natija: IndentationError: expected an indented block 
#bun kodda xatolik for dan keyingi yani ichidagi print da joy tashalmagani

# son = 50
# if son>=0:
#     print("Musbat son")
# else:
# print("Manfiy son")
#Natija: IndentationError: expected an indented block
#bun kodda xatolik else: dan keyingi yani ichidagi print da joy tashalmagani


#TypeError qatoligi
#son = input("Istalgan son kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng")
#Natija: TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#bu kodda qatolik qabul qilingan malumotni int yani son qiymatiga otqazish qolib ketgan


#NameError xatoligi
#prit("Hello World!")
#Natija: NameError: name 'prit' is not defined
#bu kodda xatolik print noto'g'ri yozilgani

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mvealar:
#     print(meva)
#Natija: NameError: name 'mvealar' is not defined
#bu kodda mevallar digan o'zgaruvchi forni ichida noto'g'ri yozilgani

#ValueError xatoligi
# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
#bunda xatolik bunda raqam so'raganida o'nlik son kiritsak xato deydi chunki raqam 
#so'ralganda int turubdi shunga shuning o'rni float qoyish kerak


# #IndexError xatoligi
# mevalar = ['olma','anor','uzum']
# print(mevalar[3])
#Natija: IndexError: list index out of range
# bu kodda 3 chi index kech narsa yoqligi uchun xato chiqaradi


#ZeroDivisionError xatoligi
# #x, y = 50, 50
# z = 250/(x-y)
#bu kodda xatolik 250likni 0 ga bo'lgan legi uchun


#MANTIQIY XATOLAR xatolik
# #son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2
# print(f"{son} ning ildizi {ildiz} ga teng")
#bu kodda xatolik ildizdagi 1/2 ni qavisni ichiga olish esdan chiqan

# #mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")
#bu kodda xatolik 2-chi print da joy tashilgani yani joyni olib tashlasa ichidagi so'z gapni oxirida 1 marta chiqadi
 