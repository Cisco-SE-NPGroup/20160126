def guessit(guess):
	if guess == number:
		print 'Congratulation!! you guess it'
		return 0
	elif guess < number:
		print 'No, it is a littel higher than that'
		return 1
	else:
		print 'No, it is a littel lower than that'
		return 2

number = 20
myResult = 1

for i in range (1,6):
	if myResult > 0:
		guess = int(raw_input('Enter an interget :'))
		myResult = int(guessit(guess))
	elif myResult == 0:
		break
else:
	print 'Sorry, you lost all your chance'


	
