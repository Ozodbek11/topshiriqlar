# a = 2
# b = 4
# c = a+b

# x,y,z = 'salom',3,4.5
# x=y=z="hello world"

# print(x,y,z,sep="+")
# print(a)
# print("1+2+3 = ",end="")
# print(1+2+3)
# x=15
# x//=3  #x=x+3
# print(int(x))
# x=5
# x**=3 #x=x**3
# print(x)
# a = False
# b = 3
# print(a >= b)
# print(a or b)
# a=11
# print (not(a>3 or a<10))

# x = ["olma", "banan"]
# y = ["olma", "banan"]
# z = y
# print(x is not y)

# x = ["audi", "mustang"]
# print("audi" in x) #true
# print("audi" not in x) #False
# a = float(input("a="))
# b = float(input("b="))
# q = a+b
# k = a*b
# bol = a/b
# ayir = a-b
# print(f"qoshish {q} ")
# a = int(input("soni"))
# a = "salom"
# print(3*a)

# starlar biLan ishlash
# list = [1,3,4,6,3,3,2]

# print(list[-4:4])

# print(str[:])
# sum  = 0
# for x in str:
#     sum+=1
#     print(sum)
#     # print(x,end="\n")
# print(sum)
# print("Gulla yashna hur \"O\'zbekistonim\"")
# print(f"salom \t qudrat")
# name = input("ismingiz")
# age = int(input("yoshingiz"))
# print("salom men {} . men {} yoshdaman".format(name,age) )
# str = "salom boqiy gijduvan"
# str1 = str.upper()

# print(str.title())       #bosh harfni katta harfga almashtiradi
# print(str1.lower())            #kichik harflarga ogiradi
# print(mystr.upper())            katta harflarga ogiradi
# print(str.swapcase())        # katta harfni kichikka ogiradi va aksincha
# print(mystr.title())            har bir sozni bosh harf bilan ogiradi
# print(str.count('o'))         #shu iboradan nechtaligini sanaydi    ///  4   ///
# print(str.endswith(''))   #oxirgi so'z shu bolsa tru qaytaradi   /// true ///
# str = "salom boqiy buxoro"

# print(str.startswith('The'))     #birinchi soz shu bolsa tru qaytaradi

# print(str.find('buxoro'))
# print(str.index('o'))            # ///   15  ////
# a="str"
# print(a.isdigit())
# print(str.rjust(30, '+'))
# mystr = '         The, quik brown fox jumps over the lazy dog'
# print(mystr.strip())  # The quik brown fox jumps over the lazy dog
# mystr = 'The, quik brown fox jumps over the lazy dog'
# print(mystr.partition('ik'))


# a = [1,2,3,4,5]

# os = ["windows","linux","MacOs"]
# os.append("dopix")
# os.insert(1,'doppi')
# os.remove("linux")
# os.pop(0)
# print(os)
# del os
# print(os)
# os.clear()
# a = os.copy()
# os.reverse()
# jadval = ['Obidov Ismoil', 'Sharopov Ruxshod', 'Axmadov Abduvoxid', 'Muxtorov Sulaymon', 'Abdulloyev Timur']
# jadval.sort()
# jadval.reverse()
# jadval2 = [1,2,3,4,5]
# jadval.extend("salom")
# print(jadval)
from math import *

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
#
# d = sqrt(b ** 2 - 4 * a * c)
# if d > 0:
#     if a > 0 or a < 0:
#         x1 = (-b + d) / 2 * a
#         x2 = (-b - d) / 2 * a
#         print(f"x1 = {x1} x2= {x2}")
#     elif a == 0:
#         print('a nolga teng bolmasligi kk')
# elif d < 0:
#     print('tenglama ildizlari yoq')
# else:
#     if a > 0 or a < 0:
#         x = -b / 2 * a
#         print(x)
#
#     elif a == 0:
#         print('a nolga teng bolmasligi kk')
# print(os.append('do\'pix'))


# lesson3

# list metodlari
# append() #Ro'yxat oxiriga element qo'shadi
# insert() Belgilangan joyga element qo'shadi
# remove() Belgilangan qiymatga ega elementni olib tashlaydi
# pop() Belgilangan holatda elementni olib tashlaydi
# del ochiradi
# list1= ['salom',1,3]
# print(list1)
# del list1[1]
# print(list1)
#  clear() Barcha elementlarni ro'yxatdan olib tashlaydi
# copy() Ro'yxatning nusxasini qaytaradi
# reverse() Reverses the order of the list
# sort() Ro'yxatni saralash
# extend() Ro'yxat elementlarini (yoki biron bir takrorlanadigan) joriy ro'yxatning oxiriga qo'shing
# os  = ["windows","linux","MacOs"]
# os.extend(["salom"])
# print(os)
#
# sum = 50
# for x in range(1,101,1):
#     print(x)
# print(sum)
# a = range(101)
# for x in a:
#     print(x)
# for x in range(-10,101,3):
#     print(x)
# for x in range(-100,0,1):
#     print(x)
# for x in range(-1,-10,-1):
#     print(x)

# for x in range(11):
#     for y in range(11):
#
#         for z in range(11):
#             print(f" x ={x}  y = {y} z = {z}")

# list = [1,2,3,4,5,6,7,8,9,10]
# for x in list:
#     print(x)
# for x in range(10,1):
#     print(x)

# for x in list:
#     print(x,end='')
# a = 'salom'
# for x in a:
#     print(a)
# a= input('soz=')
# d = {'apple':'olma','cherry':'gilos','melon':'qovun','watermelon':'tarvuz'}
# for x in d.values():
#     if x == a:
#         print(f"siz kiritgan soz mavjud")
# n = int(input('n='))
# while n != 20:
#     n+=1
#     if (n % 2) == 0:
#         print(n)
#         continue

# n = 5
# for x in range(n // 2, n + 1, +2):
#     for y in range(1, n - x, +2):
#         print(" ", end="")
#     for y in range(1,x+1):
#         print('*',end="")
#     for y in range(1, n - x + 1):
#         print(" ", end="")
#     for y in range(1, x + 1):
#         print("*", end="")
#     print()
# for x in range(n, 0, -1):
#     for y in range(x, n):
#         print(" ", end="")
#     for y in range(1, (x * 2)):
#         print("*", end="")
#     print()