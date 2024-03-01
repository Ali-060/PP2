import re

with open("row.txt") as file:
    for line in file:
        x = re.findall("[A-Z][a-z]+", line)
        print(x)