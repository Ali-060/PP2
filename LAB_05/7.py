import re

with open("row.txt") as file:
    for line in file:
        snake_case = line.strip()
        words = snake_case.split('_')
        camel_case = words[0] + ''.join(word.title() for word in words[1:])
        print(camel_case)