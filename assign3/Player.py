class Player:
	def __init__(self):
		#implement the properties here
		self.__chips = 0
		
	
	
	def add_chips(self, chips):
		if type(chips) != int or chips<1:
			raise Exception("The number of chips to add must be an integer and greater than 0")
		self.__chips += chips
		
		
	def remove_chips(self, chips):
		if type(chips) != int or chips<1:
			raise Exception("The number of chips to remove must be an integer and greater than 0")
		self.__chips -= chips
	
	
	def get_chips(self):
		return self.__chips
	
