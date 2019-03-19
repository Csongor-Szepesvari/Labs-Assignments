class Card:
	order = ("2","3","4","5","6","7","8","9","T","J","Q","K","A")
	validSuits = ("H","S","C","D")
	def __init__(self, rank, suit):
		assert rank in cls.order, "Invalid Rank"
		assert suit in cls.validSuits, "Invalid Suit"
		self.__rank = rank
		self.__suit = suit
	
	
	def get(self):
		return str(self)
	
	
	def get_rank(self):
		return self.__rank
	
	
	def get_suit(self):
		return self.__suit
	
	def __gt__(self, other):
		myVal = cls.order.index(self.get_rank())
		otherVal = cls.order.index(other.get_rank())
		return myVal > otherVal
		
		
	def __lt__(self, other):
		myVal = cls.order.index(self.get_rank())
		otherVal = cls.order.index(other.get_rank())
		return myVal < otherVal
	
	
	def __eq__(self, other):
		myVal = cls.order.index(self.get_rank())
		otherVal = cls.order.index(other.get_rank())
		return myVal == otherVal
		
	
		
	def __str__(self):
		return self.get_rank()+self.get_suit()
		
