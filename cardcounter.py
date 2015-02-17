cardstocount = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
def cardcounterplayer():
	global cardstocount
	global playercard1
	global playercard2
	global playercards
	global playertotal
	global newcards
	playertotal += cardstocount[playercard1]
	playertotal += cardstocount[playercard2]
	while playertotal < 21:
		answer = input("Would you like to hit?")
		while answer.lower() == 'yes' or answer.lower() == 'hit' or answer.lower() == 'y':
			playercard3 = random.choice(newcards)
			newcards.remove(playercard3)
			playercards.append(playercard3)
		break