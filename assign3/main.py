from Player import Player
from Table import Table

def main():
	#implement the game loop here
	menuFlag = True
	player = Player()
	while menuFlag:
		#ask player to buy play quit
		res = input("Would you like to buy chips, play a game, or quit? (b/p/q): ")
		while res.lower() not in ("b", "p", "q"):
			res = input("Would you like to buy chips, play a game, or quit? (b/p/q): ")
		if res == "b":
			num = input("How many chips would you like to buy? (up to 1000): ")
			try:
				num = int(num)
				if num>1000 or num<1:
					print("Must be below 1000 and greater than 0")
				else:
					player.add_chips(num)
			except ValueError:
				print("Must be an integer.")

def auto_play():
	#TODO

if __name__ == "__main__":
	main()
