# This program reads the content of a file

my_file = open("fruits.txt", "r")
content = my_file.read()
my_file.close()
print(content)