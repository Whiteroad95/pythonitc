# a=input("Press input your mail: ")

# y=a.count("@")

# b=a.split("@")

# if y!=0:
#     c=b[1]
#     if y!=0:
#         if c=="gmail.com" or c=="mail.ru":
#             print("Mail is correct")
#             x=input ("Your number is 123456, Please Enter this code: ")
#             if x=="123456":
#                 print("Correct code")

#             else:
#                 print("UNcorrect code")   
#         else:
#             print("Mail is NOOOT correct")   

#     else:
#         print('Please Enter using "@"')    

# else:
#     print('Please Enter using "@"')    




# a=int(input("How much is 7 * 7 ? "))
# if a==49:
#     print("Correct")
#     b=int(input("How much is 4 * 5 ? "))
#     if b==20:
#         print("Correct")
#     else:
#           print("UNCorrect")     
# else:
#     print("UNCorrect")    





# a=False or(True or(2<3))
# b=(2>3) and(3<4) or True
# c=(not True or 5**2!=1000)and not False
# print(a)
# print(b)
# print(c)



# yoda=['on Python', 'programing ','I like ']
# a=yoda[2]
# b=yoda[1]
# c=yoda[0]
# d=a+b+c
# print(d)






wather_dict = {'base': 'stations',
  'clouds': {'all': 100},
  'datetime': '2022-10-26 11:33:21.774524',
  'main': {'feels_like': 6.57,
           'grnd_level': 925,
           'humidity': 71,
           'pressure': 1022,
           'sea_level': 1022,
           'temp': 9.18,
           'temp_max': 9.18,
           'temp_min': 9.18},
  'name': 'Almaty',
  'rain': {'1h': 1.26},
  'sys': {'country': 'KZ', 'sunrise': 1666747131, 'sunset': 1666785198},
  'timezone': 21600,
  'visibility': 10000,
  'weather': [{'description': 'moderate rain',
               'icon': '10d',
               'id': 501,
               'main': 'Rain'}],
  'wind': {'deg': 262, 'gust': 9.09, 'speed': 4.99}}

date=wather_dict['datetime']
date_new=date[:10]
date_new2=date[11:16]
almaty=wather_dict['name']
temp=wather_dict['main']['temp']
opis=wather_dict['weather'][0]['description']
cloud=wather_dict['clouds']['all']
vlaga=wather_dict['main']['humidity']
davl=wather_dict['main']['pressure']
veter=wather_dict['wind']['speed']

print(f'Data: {date_new}')
print(f'Vremya: {date_new2}')
print(f'Pogoda v gorode: {almaty}')
print(f'Temperatura: {temp} °C')
print(f'Opisanie: {opis}')
print(f'Oblachnost {cloud}')
print(f'Vlazhnost {vlaga}')
print(f'Davleniye {davl} мм.рт.ст')
print(f'Skorost Vetra {veter}')





# a=input("Press input your first: ")
# b=input("Press input your second: ")
# c=input("Press input your third: ")
# range_a=len(a+b+c)

# a_list=[] 

# a_list.append(a)
# a_list.append(b)
# a_list.append(c)
# print(a_list)
# print(range_a)

# if range_a>20:
#     if len(a)>len(b) and len(a)>len(c):
#         a_list.pop(0)
#     elif len(b)>len(c) and len(b)>len(a):
#         a_list.pop(1)   
#     elif len(c)>len(a) and len(c)>len(b):
#         a_list.pop(2)      

# print(a_list)