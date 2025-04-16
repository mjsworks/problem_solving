from extendedShopping import Eshopcart

cart = Eshopcart(["milk","bread", "eggs", "potatoes"])

print(cart)
print(repr(cart))
print(len(cart))

for i in range(len(cart)):
    print(cart[i])