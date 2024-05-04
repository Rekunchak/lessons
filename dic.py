a = [3, 2, 0]
a.append(9)
print(a)
a.remove(0)
print(2 in(a))
a.sort()
print(a)
product = {
 "city" : "Москва", 
 "temperature" : 20,
 "age": 40
 }
print(product["city"])
product["temperature"] -= 5 
#print(len(product))
print(product.get("country", "Россия"))
product["date"] = "27/05/2019"
print(product)
print(len(product))