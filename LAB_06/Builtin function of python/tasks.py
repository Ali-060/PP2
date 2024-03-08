# 1
import math
def multiply_list(numbers):
    return math.prod(numbers)

my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)
print(result)

# 2
def count_upper_lower(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

input_string = input()
upper, lower = count_upper_lower(input_string)
print(upper, lower)

# 3
input_string = input()
if input_string == input_string[::-1]:
    print("It's palindrome")
else:
    print("No, it't not")

# 4
import time
def root(x, y):
    time.sleep(y/1000)
    print(f"Square root of {x} after {y} miliseconds is {x ** 0.5}")

input_number = int(input())
input_milisec = int(input())
root(input_number, input_milisec)

# 5
elements = (True, False, True, False)
print(all(elements) is True)