import re

file = open('sample.txt')
raw = file.read()
x = re.findall('[0-9]+', raw)
numbers = list()
for num in x:
    num = int(num)
    numbers.append(num)
print(sum(numbers))
