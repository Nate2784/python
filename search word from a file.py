# variables
count = 0
i = 1
# recieves file name with extension
Fname= input("Enter file you want to search in with extension!: ")
# error handeling
try:
    fhand = open(Fname)
except:
    print("file not found in path, please add a file into the same directory and try again with the appropriate name. \nthank you!")
    quit()
# recieves the word to search in lines
word = input("Enter a word you want to search: ")
#  a for loop to find lines which have the user input word in them and prints them out
for line in fhand:
    line = line.rstrip()
    # checks wethyer the word is in the line or not if not it returns to fo loop
    if not word in line:
        continue
    count +=1
    print(i,line)
    i+=1
print(f"LInes that contain the word {word}: total =",count)