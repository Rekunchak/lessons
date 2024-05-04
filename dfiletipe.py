a={
    "city": "Moscow",
    'temperature': 20,
}
print(a['city'])
a['temperature']-=5
a['country'] = "Russia"
print(a.get('country', "Russia"))
a['date']= '27.05.2020'
print(a)
print(type(a))
g= "    СТАС   ".strip().capitalize()
c= f"Привет {g}"
print(c)
print(type(c))
#print(len(c))
#c=c.strip()
#print(c.split(), len(c))
#b = input("Сколько вам лет? ")
#print(type(b))
#age = 2024 - int(b)
#print(f"Вы родились в  {age} году")