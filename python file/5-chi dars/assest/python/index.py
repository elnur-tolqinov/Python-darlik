# Matnlarni qo'shish uchun + operatoridan qo'yamiz:
ism = 'Ahmad'
print("Mening ismim " + ism)
# Natija: Mening ismim Ahmad

ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)
# Natija: AhadQayum

ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shish
# Natija: Ahad Qayum

# matinlarni qo'shishda f-string usulidan  f"{matn1} {matn2}" ham foydalansa bo'ladi:
ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

#Bu usul yordamida uzun matnlarni ham yasash mumkin:
ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
#Natija: Salom, mening ismim Bond. James Bond!

print('Hello World!')
print('Hello \tWorld!') #bunda /t bitta tab tashab yozadi
print('Hello \nWorld!') #bunda /n matnini keyingi qatorga uzub joylashtiradi

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper()) #upper() metodi matndagi har bir harfni katta harfda ko'rsatadi.
#Natija: AHAD QAYUM

ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower()) #lower() metodi esa aksincha, har bir harfni kichik harfda ko'rsatadi. 
#Natija: ahad qayum

ism_sharif = 'james bond'
print(ism_sharif.title()) #title() metodi matndagi har bir so'zning birinchi harfini katta harfda ko'rsatadi. 
#Natija: James Bond

ism_sharif = 'james bond'
print(ism_sharif.capitalize()) #capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
#Natija: James bond

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman") #lstrip() — matn boshidagi bo'shliqni,
#Natija: Men olma      yaxshi ko'raman 
print("Men " + meva.rstrip() + " yaxshi ko'raman") #rstrip() – matn oxiridagi bo'shliqni,
#Natija: Men       olma yaxshi ko'raman 
print("Men " + meva.strip() + " yaxshi ko'raman")  #strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
#Natija: Men olma yaxshi ko'raman 
print("Men " + meva + " yaxshi ko'raman")
#Natija: Men       olma      yaxshi ko'raman

