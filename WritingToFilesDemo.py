#f = open("data.txt","w")
f = open("data.txt","a")
#a = appended to file, it gets added along
#with the the other/previous results

#f.write("Line 1\n")
#f.write("Line 2\n")

name = input("What is your name: ")
age = input("What is your age: ")

f.write(name + "\n")
f.write(age + "\n")


f.close()