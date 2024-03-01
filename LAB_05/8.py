import re

with open("row.txt") as file:
    for line in file:
        words = re.findall('[A-Z][a-z]*', line)
        print(words)