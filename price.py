price = 100
discount = 20
def discounted(price, discount, maxdiscount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    maxdiscount = abs(float(maxdiscount))
    if maxdiscount >= 99:
        raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= maxdiscount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

product = {"name": "Samsung", "stock": 8, "price": 10000, "discount": 50}
product["price_with_discount"] = discounted(product["price"], product["discount"])
print(product)
print(discounted(100, 50, 100))