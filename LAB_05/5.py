import re

with open("row.txt") as file:
    for line in file:
        x = re.findall("a.*b$", line)
        print(x)