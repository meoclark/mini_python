import random

ran_num = random.randint(1,10)
player = None
while True:
	player = int(input("Guess a number between 1 and 10: "))
	if player < ran_num:
		print("TOO LOW!")
	elif player > ran_num:
		print("TOO HIGH!")
	else:
		print("YOU WON!")
		play_again = input("do you want to play again? (y/n) ")
		if play_again == "y":
			ran_num = random.randint(1,10)
			player= None
		else:
			print("Thank you for playing!")
			break