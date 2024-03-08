# 1
degree = int(input())
'''
by the PI = rad * 180 / degree
where 
rad = 0.261904
deg = 15
'''
pi = 3.142848
print(pi * degree / 180)

# 2
height = int(input())
base_1 = int(input())
base_2 = int(input())
print((base_1 + base_2) * height / 2)

# 3
import math
sides = int(input())
a = int(input())
print((sides * a ** 2) / (4 * math.tan(math.pi / sides)))

# 4
a = int(input())
height = int(input())
print(a * height)