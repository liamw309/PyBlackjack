playercard1 = 0
playercard2 = 0
playercards = []
playertotal = 0
def player():
	global playercard1
	global playercard2
	global newcards
	global playercards
	playercard1 = random.choice(newcards)
	newcards.remove(playercard1)
	playercard2 = random.choice(newcards)
	newcards.remove(playercard2)
	playercards.append(playercard1)
	playercards.append(playercard2)
	return playercards
	return playercard1
	return playercard2
player()