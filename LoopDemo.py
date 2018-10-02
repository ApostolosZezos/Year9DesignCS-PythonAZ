#A loop is a programming structure that can repeat a section of code
#A loop can run the same code exactly over and over or
#with some thought it can generate a pattern

#There are two broad categories of loops
# Condiotional Loops (while):	These loop as long as the condiotion is true

# Counted Loops (for):	These loop using a counter to keep track of how many 
#						the loop has run
#
#
# You can use any loop in any situation, usually from a design
# persepctive there is aa better loop in terms of coding.
#
# If you know in advance how many times a loop should run a COUNTED LOOP 
# is usually the better choice
#
# If you don't know how many thimes a loop should run a CONDITIONAL LOOP 
# is usually the better choice

print("************************************************************")
#Taking Inputs


word = ""

#A while loop evaluates a condition when it is first reached 
#If the condition is true it enters the loop block
while (len(word) < 6 or word.isalpha() == False):
	#loop block
	
	word = input("Please input a word larger than 5 letters: ")
	#print(word.isalpha())
	if (len(word) < 6):
		print("Dude I said more than 5 letters!")

	if (word.isalpha() == False):
		print("Dude I said a real word!") 
#When we reach the bottom of the loop block we check the condition again.
		#check condition at the bottom of loop block

	#If it is true, we go back to the top of the block and run it again.	
		#if true loop starts again



print(word + " is a seriously long word!")