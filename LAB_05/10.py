import re

with open("row.txt") as file:
    for line in file:
        camel_case = line.strip()
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
        print(snake_case)