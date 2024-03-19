with open("dict.txt", "r") as file:
    file = file.readlines()
    
data = (set([word[:-1] for word in file]))

with open("dict.txt", "w") as file:
    for row in data:
        file.write(row+"\n")