import math
c = int(input("введите гипотенузу: "))
a = int(input("введите катет: "))
b = math.sqrt(c**2 - a**2)
print("катет=",b)
