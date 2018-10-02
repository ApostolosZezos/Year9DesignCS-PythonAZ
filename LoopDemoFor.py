print("************************************************************")
print("Counted Loops: For")

print("0")
print("1")
print("2")
print("3")

#When we think of a for loop I want you to thimk about
	# Count: The variable that holds the current count
	# Check: The check that is done each time the loop runs
	# Change: The change applied to the count each time the loop runs

#Challenge with python is the check is assumed for you. 
#Meaning <initial value> is less tham your <check value>

#for <count var> in range (<initial value, <check value>, <change>):
print("************************************************************")
#i = 0, 0 < 4, True RUN LOOP
#i = 1, 1 < 4, True RUN LOOP
#i = 2, 2 < 4, True RUN LOOP
#i = 2, 2 < 4, True RUN LOOP
#i = 3, 4 < 4, True RUN LOOP
#i = 4, 4 < 4, False EXIT AND CONTINUE
for i in range(0,40000000000,1):
	print(i)
	if ( i % 2 == 0):
		print(str(1) + " is even")
	else:
		print(str(i) + " is odd")