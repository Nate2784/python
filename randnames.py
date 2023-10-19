import random
import string


letters = {i: letter for i, letter in enumerate(string.ascii_lowercase, 1)}

def generate_name(length):
    name = ''
    for _ in range(length):
        
        random_num = random.randint(1, 26)
        
        name += letters[random_num]
    return name


random_name = generate_name(10)
print(random_name)

# squares ={i: i**2 for i in range(1,10)}
# print(squares)