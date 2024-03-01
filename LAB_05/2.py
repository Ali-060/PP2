import re

with open("row.txt") as file:
    for line in file:
        x = re.findall("ab{2,3}", line)
        print(x)