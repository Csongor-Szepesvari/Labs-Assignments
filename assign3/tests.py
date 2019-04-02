from Card import Card
from Player import Player
from Table import Table
from queue import Queue


def test_card():
	#Creates a card which is the Ace of Diamonds
	my_card = Card("A", "D")
	
	#tests get function
	assert my_card.get() == "AD", "Invalid card"
	#tests rank function
	assert my_card.get_rank() == "A", "Invalid rank"
	#tests suit function
	assert my_card.get_suit() == "D", "Invalid suit"
	
	#tests a rank convertion function
	assert my_card.convert_rank("A") == 14, "Invalid conversion"
	assert my_card.convert_rank("K") == 13, "Invalid conversion"
	assert my_card.convert_rank("Q") == 12, "Invalid conversion"
	assert my_card.convert_rank("J") == 11, "Invalid conversion"
	assert my_card.convert_rank("T") == 10, "Invalid conversion"
	assert my_card.convert_rank("9") == 9, "Invalid conversion"
	assert my_card.convert_rank("8") == 8, "Invalid conversion"
	assert my_card.convert_rank("7") == 7, "Invalid conversion"
	assert my_card.convert_rank("6") == 6, "Invalid conversion"
	assert my_card.convert_rank("5") == 5, "Invalid conversion"
	assert my_card.convert_rank("4") == 4, "Invalid conversion"
	assert my_card.convert_rank("3") == 3, "Invalid conversion"
	assert my_card.convert_rank("2") == 2, "Invalid conversion"
	
	#tests that the suit has no influence on comparison __eq__
	assert Card("A","D") == Card("A","S") == Card("A","H") == Card("A","C"), "Invalid comparison =="
	
	#tests rank comparison function _gt__
	assert Card("A","H") > Card("K", "H") > Card("2", "S"), "Invalid comparison >"
	
	#tests the __str__ function
	assert str(my_card) == "AD", "Invalid string"
	
	#returns True to sinalize that it has passed all tests	
	return True

def test_player():
	myPlayer = Player()
	
	#see if the initial chips are 0
	assert myPlayer.get_chips() == 0, "not init to 0"
	
	#test adding chips
	myPlayer.add_chips(10)
	assert myPlayer.get_chips() == 10, "failed adding"
	
	#test removing chips
	myPlayer.remove_chips(110)
	assert myPlayer.get_chips() == -100, "failed removing"

def test_table():
	myT = Table()
	q = Queue()
	q.put(Card("A", "D"))
	q.put(Card("Q", "S"))
	myT.set_shoe(q)
	
	#test bet setting and getting
	myT.set_bet(100)
	assert myT.get_bet() == 100
	
	#test clearing of cards from dealer and player, test card getting
	myT.draw_card("player")
	myT.draw_card("dealer")
	assert str(myT.get_card("player")) == "AD", "failed to draw"
	assert str(myT.get_card("dealer")) == "QS", "failed to draw"
	myT.clear()
	assert myT.get_card("player") == None, "failed to clear"
	assert myT.get_card("dealer") == None, "failed to clear"
	assert str(myT.get_discard().get()) == "AD", "discard queue broken"
	assert str(myT.get_discard().get()) == "QS", "discard queue broken"
	
	#test resetting discard
	myT.get_discard().put(Card("2", "H"))
	myT.clear_discard()
	assert myT.get_discard().empty(), "failed to wipe discard"
	
	
	#test shoe making
	myT.set_shoe(myT.make_shoe())
	#print(myT.shoe_to_list())
	#print(myT.get_shoe_size())
	assert myT.get_shoe_size() == 6 * 52, "not full"
	aList = []
	for i in range(myT.get_shoe_size()):
		aList.append(str(myT.get_shoe().get()))
	aList = list(set(aList))
	myT.validate_deck(aList)
	
	#test result checker
	assert myT.resolve_round(Card("A", "D"), Card("A", "S")) == 0, "Should've tied"
	assert myT.resolve_round(Card("2", "D"), Card("A", "S")) == -1, "Player should've lost"
	assert myT.resolve_round(Card("A", "D"), Card("2", "S")) == 1, "Player should've won"
	
	
test_card()
test_player()
test_table()
