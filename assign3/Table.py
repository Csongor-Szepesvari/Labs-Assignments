from Card import Card
from random import shuffle
from queue import Queue

class Table:
	acceptable = []
	for rank in Card.order:
		for suit in Card.validSuits:
			acceptable.append(rank+suit)	
	def __init__(self):
		self.__player_card = None
		self.__dealer_card = None
		self.__discard = Queue()
		self.__shoe = None
		self.__bet = 0

	
	def resolve_round(self, player, dealer):
		if player > dealer:
			return 1
		elif player < dealer:
			return -1
		else:
			return 0
	
	
	def set_bet(self, bet):
		assert type(bet) == int, "Bet must be an integer"
		assert bet>=0, "Bet must not be negative"
		self.__bet = bet
	
	
	def get_bet(self):
		return self.__bet
	
	
	def clear(self):
		self.discard.put(self.__player_card)
		self.__player_card = None
		self.discard.put(self.__dealer_card)
		self.__dealer_card = None
	
	
	def create_deck(self):
		myDeck = []
		for rank in Card.order:
			for suit in Card.validSuits:
				myDeck.append(Card(rank, suit))
		return myDeck


	def validate_deck(self, deck):
		if len(deck) != 52:
			raise Exception("Deck must have 52 cards in it.")
		for card in deck:
			if str(card).upper() not in cls.acceptable:
				raise Exception("%s is not a valid card." % str(card))
		return True	

	def make_shoe(self):
		bigDeck = []
		for i in range(6):
			bigDeck.append(self.create_deck())
			self.validate_deck(bigDeck[i])
			shuffle(bigDeck[i])
		q1 = Queue()
		q2 = Queue()
		q3 = Queue()
		for i in range(6):
			for card in bigDeck[i]:
				if i<3:
					q1.put(card)
				else:
					q2.put(card)
		
		for i in range(6):
			intermediateL = []
			for j in range(26):
				intermediateL.append(q1.get())
				intermediateL.append(q2.get())
			shuffle(intermediateL)
			for card in intermediateL:
				q3.put(card)
		return q3
			
	def set_shoe(self, shoe):
		self.__shoe = shoe
	
	

		
		

	

