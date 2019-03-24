from Player import Player
from Table import Table

def main():
#implement the game loop here
    global menuFlag
    global tBet
    global bet
    global profit
    global player
    global table
    global totalGames
    global totalHands
    global wars
    global winningHands
    while menuFlag:
        if table.get_shoe_size() < 52:
            table.set_shoe(table.make_shoe())
            table.clear_discard()
	#ask player to buy play quit
        print("You currently have %d chips." % player.get_chips())
        res = input("Would you like to buy chips, play a game, or quit? (b/p/q): ")
        while res.lower() not in ("b", "p", "q"):
            res = input("Would you like to buy chips, play a game, or quit? (b/p/q): ")
        if res == "b":
            num = input("How many chips would you like to buy? (1-1000): ")
            try:
                num = int(num)
                if num>1000 or num<1:
                    print("Must be between 1-1000")
                else:
                    player.add_chips(num)
            except ValueError:
                print("Must be an integer.")
        elif res == "q":
            menuFlag = False
            print("You played %d hands;" % totalHands)
            if totalGames>0:
                print("your average bet was %.3f;" % (tBet/totalGames))
                print("your average profit was %.3f throughout the session;" % (profit/totalGames))
            else:
                print("your average bet was 0;")
                print("your average profit was 0 throughout the session;")
            if totalHands>0:
                print("you had %d winning hands which amounts to %.3f percent of the time;" % (winningHands, (100*winningHands/totalHands)))
            else:
                print("you had %d winning hands which amounts to 100 percent of the time;" % (winningHands))
            print("and you went to war %d times." % wars)
        elif player.get_chips()>1:
            #get a successful bet
            successfulBet = False
            while not successfulBet:
                bet = input("Place your bet (between 2-100, only even numbers): ")
                try:
                    bet = int(bet)
                except ValueError:
                    print("Your bet must be an integer")
                else:
                    if bet>=2 and bet<=100 and bet%2==0 and bet<=player.get_chips():
                        print("Bet placed successfully.")
                        successfulBet = True
                        table.set_bet(bet)
                        tBet += bet
                    else:
                        print("Unsuccessful bet.")
	    #finish bet successfully
	    #deal cards one to each
            table.draw_card("player")
            table.draw_card("dealer")
            totalHands += 1
            totalGames += 1
            print("Player shows", str(table.get_card("player"))+",", "dealer shows", table.get_card("dealer"))
            result = table.resolve_round(table.get_card("player"), table.get_card("dealer")) #1 = player won, -1 loss, 0 = tie
            if result == 1:
                print("Player wins %d chips." % table.get_bet())
                player.add_chips(table.get_bet())
                winningHands += 1
                profit += table.get_bet()
            elif result == -1:
                print("Player loses %d chips." % table.get_bet())
                player.remove_chips(table.get_bet())
                profit -= table.get_bet()
	    #tie scenario go to war or surrender
            else:
                doubleDown = input("Tie! Either surrender or go to war -- double your bet, a tie or victory results in you gaining the initial bet, a loss means you lose double.(w/s): ")
                while doubleDown.lower() != "w" and doubleDown.lower() != "s":
                    doubleDown = input("War or surrender. (w/s): ")
                if doubleDown.lower() == "w" and player.get_chips()>=table.get_bet()*2:
                    wars += 1
                    totalHands += 1
                    table.set_bet(table.get_bet()*2)
                    table.clear()
                    table.burn()
                    table.draw_card("player")
                    table.draw_card("dealer")
                    print("Player shows", str(table.get_card("player"))+",", "dealer shows", table.get_card("dealer"))
                    result = table.resolve_round(table.get_card("player"), table.get_card("dealer"))
                    if result == 1 or result == 0:
                        print("Player wins %d chips." % table.get_bet()//2)
                        player.add_chips(table.get_bet()//2)
                        profit += table.get_bet()//2
                        winningHands += 1
                    else:
                        print("Player loses %d chips." % table.get_bet())
                        player.remove_chips(table.get_bet())
                        profit -= table.get_bet()
                else:
                    player.remove_chips(table.get_bet()//2)
                    profit -= table.get_bet()//2
            table.clear()
        print()    
		

def auto_play(action, amount):
    global menuFlag
    global tBet
    global bet
    global profit
    global player
    global table
    global totalGames
    global totalHands
    global wars
    global winningHands    
    if action.lower() == "q":
        menuFlag = False
        outList = []
        if totalGames>0:
            outList = [totalHands, (tBet/totalGames), (profit/totalGames), winningHands, (winningHands/totalHands)*100, wars]
        else:
            outList = [totalHands, 0, 0, winningHands, None, wars]
        return outList
    
    elif action.lower() == "b":
        if amount>=1 and amount<=1000:
            player.add_chips(amount)
            return True
        else:
            return False
	
    elif action.lower() == "p":
        table.set_bet(amount)
        table.draw_card("player")
        table.draw_card("dealer")
        totalHands += 1
        totalGames += 1
        result = table.resolve_round(table.get_card("player"), table.get_card("dealer")) #1 = player won, -1 loss, 0 = tie
        if result == 1:
            player.add_chips(table.get_bet())
            winningHands += 1
            profit += table.get_bet()
        elif result == -1:
            player.remove_chips(table.get_bet())
            profit -= table.get_bet()
	#tie scenario go to war or surrender
        else:
            if player.get_chips()>=table.get_bet()*2:
                wars += 1
                totalHands += 1
                table.set_bet(table.get_bet()*2)
                table.discard("player")
                table.discard("dealer")
                table.burn()
                table.draw_card("player")
                table.draw_card("dealer")
                result = table.resolve_round(table.get_card("player"), table.get_card("dealer"))
                if result == 1 or result == 0:
                    player.add_chips(table.get_bet()//2)
                    profit += table.get_bet()//2
                    winningHands += 1
                else:
                    player.remove_chips(table.get_bet())
                    profit -= table.get_bet()
            else:
                player.remove_chips(table.get_bet()//2)
                profit -= table.get_bet()//2
        table.discard("player")
        table.discard("dealer")	
        return player.get_chips()
    else:
        return -1
	
	

if __name__ == "__main__":
    menuFlag = True
    player = Player()
    table = Table()
    table.burn()
    totalGames = 0
    totalHands = 0
    wars = 0
    winningHands = 0
    profit = 0
    bet = 0
    tBet = 0    
    main()
