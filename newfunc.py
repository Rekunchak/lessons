def new(first, second, delimiter="&"):
    first = str(first)
    second = str(second)
    delimiter = str(delimiter)
    res = first + delimiter + second
    return res

one = new("Learn", "Python")
print(one.upper())

def format_price(price):
    price = int(price)
    r = f"Цена {price} рублей."
    return r
print(format_price(56.7))