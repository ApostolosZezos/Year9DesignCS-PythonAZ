
f = open("data.txt", "r")

content = f.read()
print(content)

list = content.split("\n")
#list = content.split(":")
print (list)