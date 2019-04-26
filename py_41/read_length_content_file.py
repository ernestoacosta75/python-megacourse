myfile = open("fruits.txt", "r")
content = myfile.read()
myfile.close()
content = content.splitlines()

for word in content:
    print(word, "-->Length: ", len(word))