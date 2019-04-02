class Card:
	order = ("2","3","4","5","6","7","8","9","T","J","Q","K","A")
	validSuits = ("H","S","C","D")
	def __init__(self, rank, suit):
		assert rank in Card.order, "Invalid Rank"
		assert suit in Card.validSuits, "Invalid Suit"
		self.__rank = rank
		self.__suit = suit
	
	
	def get(self):
		return str(self)
	
	
	def get_rank(self):
		return self.__rank
	
	
	def get_suit(self):
		return self.__suit
	
	def convert_rank(self, rank):
		return Card.order.index(rank)+2
	
	def __gt__(self, other):
		myVal = Card.order.index(self.get_rank())
		otherVal = Card.order.index(other.get_rank())
		return myVal > otherVal
		
		
	def __lt__(self, other):
		myVal = Card.order.index(self.get_rank())
		otherVal = Card.order.index(other.get_rank())
		return myVal < otherVal
	
	
	def __eq__(self, other):
		myVal = Card.order.index(self.get_rank())
		otherVal = Card.order.index(other.get_rank())
		return myVal == otherVal
		
	
		
	def __str__(self):
		return self.get_rank()+self.get_suit()
		
