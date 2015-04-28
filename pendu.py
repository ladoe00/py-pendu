import random, sys

print "Bienvenu a Py-Pendu!"

with open('words.lst', 'r') as inputFile:
	listOfWords = inputFile.readlines()
inputFile.close()

listSize = len(listOfWords)
rand = random.randint(0, listSize)

randomWord = listOfWords[rand]
guessWord = empty(len(randomWord))
guessWord[:] = '_'
print("Essaie de deviner le mot." + randomWord)
for i in range(0, len(randomWord)):
	print "_ ",
print

letter = sys.stdin.read(1)
print ("you said: " + letter)

