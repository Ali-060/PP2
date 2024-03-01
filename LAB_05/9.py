import re

with open("row.txt") as file:
    for line in file:
        spaced_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', line.strip())
        print(spaced_string)