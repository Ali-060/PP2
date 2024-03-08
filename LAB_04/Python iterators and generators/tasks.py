# 1
def squares_generator(N):
    for i in range(N):
        yield i ** 2
N = int(input())
squares = squares_generator(N)
for square in squares:
    print(square)

# 2
def even_numbers_generator(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i
N = int(input())
even_numbers = even_numbers_generator(N)
print(','.join(map(str, even_numbers)))

# 3
def divisible_by_three_and_four_generator(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
N = int(input())
divisible_numbers = divisible_by_three_and_four_generator(N)
for num in divisible_numbers:
    print(num)

# 4
def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input())
b = int(input())
squares = squares_generator(a, b)
for square in squares:
    print(square)
    
# 5
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
countdown = countdown_generator(n)
for number in countdown:
    print(number)