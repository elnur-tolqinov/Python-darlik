#XUSUSIYATLARGA STANDART QIYMAT BERISH
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1 #standart qiyamt
    
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "  
#Endi, Talaba klassidan yangi obyekt yaratganimizda har bir yangi talabaning kursi yani bosqichi 1 ga teng bo'ladi.
talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_info())
#Natija: Alijon Valiyev. 1-bosqich talabasi

#STANDART QIYMATNI O'ZGARTIRISH
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

talaba1.set_bosqich(3) #talaba1.set_bosqich(3) bu kodda 3ni o'rni raqam yozib bosqichini o'zgartirsa boladi
print(talaba1.get_info())
#Natija: Alijon Valiyev. 3-bosqich talabasi


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
#update_bosqich() metodi chaqirilganida talabning bosqichi 1 qoshilib borib  boradi:

talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_info())

talaba1.update_bosqich() # 1 bosqichga oshiramiz
print(talaba1.get_info())
#Natija: Alijon Valiyev. 1-bosqich talabasi
talaba1.update_bosqich() # update_bosqich() shu fubksiyani yozsak endi 1 bosqichga oshiramiz 
print(talaba1.get_info())
#Natija: Alijon Valiyev. 2-bosqich talabasi


#OBYEKTLAR O'RTASIDA MUNOSABAT
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)

#Talabalarni yangi fanimizga qo'shamiz:
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar_soni)
#Natija: 3  
#ro'yhatdga 3 ta talaba qo'shildi

#ro'yhatga qo'shilgan talabalarni ko'rish
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

[talaba.get_info() for talaba in self.talabalar]

mat_talabalar = matematika.get_students()
print(mat_talabalar)
#['Alijon Valiyev. 1-bosqich talabasi ', 'Hasan Alimov. 1-bosqich talabasi ', 'Akrom Boriyev. 1-bosqich talabasi ']


#dir() funksiyasi
#dir() funksiyasi yordamida istalgan obyekt yoki klassning xususiyatlari va metodlarini ko'risatadi
dir(Talaba)
#Natija
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'get_age',
#  'get_fullname',
#  'get_info',
#  'get_lastname',
#  'get_name',
#  'set_bosqich',
#  'update_bosqich']

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
#Natija: ['get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'set_bosqich', 'update_bosqich']

print(see_methods(talaba1))
#Natija: ['bosqich', 'familiya', 'get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'ism', 'set_bosqich', 
#'tyil', 'update_bosqich']