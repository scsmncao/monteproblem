from random import randint

def main():

	play = raw_input('Enter g for game or s for statistics: ')

	if play == 'g':
		monteProblem(False, True)

	if play == 's':

		iterations = int(raw_input('Enter the number of interations you want to run the game: '))

		switchWins = 0
		noSwitchWins = 0

		for i in range(0, iterations):
			if monteProblem(True):
				switchWins += 1

		for i in range(0, iterations):
			if monteProblem(False):
				noSwitchWins += 1

		print('When the player switched, he won %.2f percent of the time' % (100 * switchWins/float(iterations)))
		print('When the player didn\'t switch, he won %.2f percent of the time' % (100 * noSwitchWins/float(iterations)))

# takes in whether or not we want the player to switch
def monteProblem(switch, game=False):
	doors, car = getRandomSampleOfDoors()

	if game:
		printDoors = ['Door 1', 'Door 2', 'Door 3']
		print(printDoors)
		userChosen = int(raw_input('Pick a Door: ')) - 1

	else:
		# user chooses a random number
		userChosen = randint(0,2)

	# choose a random door to open thats not the user's or car door
	openDoor = randint(0,2)
	while (openDoor == userChosen or openDoor == car):
		openDoor = randint(0,2)

	if game:
		printDoors[openDoor] = 'Sheep'
		print(printDoors)
		print('The host opened up door %i and has a Sheep in it.' % (openDoor + 1))
		switchDoors = raw_input('Would you like to switch doors? y or n\n').lower()
		if (switchDoors == 'y' or switchDoors == 'yes'):
			switch = True
		else:
			switch = False

	# if we want to switch, take the number thats not the door or the chosen number
	if switch:
		for i in range(0,3):
			if (i != userChosen and i != openDoor):
				userChosen = i
				break
	if game:
		print('You chose to open door %i' % (userChosen + 1))

		if doors[userChosen]:
			print('You win a car!')
		else:
			print('You lose and get a Sheep')

		for i in range(0,3):
			if doors[i]:
				printDoors[i] = 'Car'
			else:
				printDoors[i] = 'Sheep'

		print(printDoors)

	return doors[userChosen]

# initializes the doors randomly and returns the car position
def getRandomSampleOfDoors():
	car = randint(0,2)
	doors = [False, False, False]
	doors[car] = True
	return doors, car

if __name__ == "__main__":
    main()