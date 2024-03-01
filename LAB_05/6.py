import re

with open("row.txt") as file:
    for line in file:
        x = re.sub(r'[ ,.]', ':', line)
        print(x)