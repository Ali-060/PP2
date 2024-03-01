import re

with open("row.txt") as file:
    for line in file:
        x = re.findall("[a-z]+_[a-z]+", line)
        print(x)