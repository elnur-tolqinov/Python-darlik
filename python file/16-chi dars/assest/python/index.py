#LUG'ATLAR RO'YXATI 
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

car = car0
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")

car = car2
print(f"{car['model'].title()},\
  {car['rang']} rang,\
  {car['yil']}-yil, {car['narh']}$")  
#Natija:
#Lacetti, oq rang, 2018-yil, 13000$ kabi hammasi shu ko'rinishda chiqadi

print(car[0])
#Natija: {'model': 'lacetti', 'rang': 'oq', 'yil': 2018, 'narh': 13000, 'km': 50000, 'korobka': 'avtomat'}

print(car[0]['model'])
#Natija: lacetti

print(f"{car[2]['rang'].title()} "
      f"{car[2]['model']}")
#Natija: Qizil gentra

malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
#bu kodda 10 ta royhat yaratildi

for malibu in malibus[:3]:
    malibu['rang']='qizil'
#bu kodda 0 chi indexdan 3 gacha malibu rangi qizilga o'zgartirlidi

for malibu in malibus[3:6]:
    malibu['rang']='qora'
#bu kodda 3 chi indexdan 6 gacha malibu rangi qoraga o'zgartirlidi

for malibu in malibus[6:]: # ohirgi 4 ta mashinani
    malibu['rang']='qora'  # rangi qora
    malibu['korobka']='mexanika' # korobkasi mexanika
#bu kodda 6 chi indexdan ohirgach gacha malibu karobkasi mexanikaga o'zgartirlidi

for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000
#bu kodda karobkasi avto bo'lsa narhi 40000 karobka mexanika bo'lsa 35000 o'zgartirlidi

#Lug'at ichida ro'yhat
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
#Natija:
#Ali quyidagi dasturlash tillarini biladi:
#PYTHON 
#C++
#hammasi shu ko'rinishda chiqadi

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='') #end='' yondagi bo'sh oldi olib yon mayon qilib qo'yadi
#Natija:
#Ali quyidagi dasturlash tillarini biladi: PYTHON C++
#hammasi shu ko'rinishda chiqadi


#Lug'at ichida lug'at
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
#Natija:
#Ali Valiyev, 1995-yilda tug'ulgan. Ma'lumoti: oliy. 
#Quydagi dasturlash tillarini biladi:
#PYTHON
#C++
#hammasi shu ko'rinishda chiqadi