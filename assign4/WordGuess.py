import random
from SecretWord import SecretWord

class WordGuess:
    def __init__(self, wordDic):
        self.wordDic = wordDic
        self.word = self.chooseSecretWord()
        self.mySecretWord = SecretWord()
        self.mySecretWord.setWord(self.word)
        #print("got to editDistance")
        self.guesses = min(max(self.editDistance(self.mySecretWord.copy(),self.mySecretWord.sort())*2, 5), 15)
        self.guessed = []

    def play(self):
        self.__init__(self.wordDic)
        """ Plays out a single full game of Word Guess """
        notDone = True
        won = False
        print("A secret word has been randomly chosen!")
        while notDone:
            print("You have %d guesses remaining" % self.guesses)
            print("Word Guess Progress: %s" % self.mySecretWord.printProgress())
            guess = self.getGuess()
            if guess == "*":
                print("Hint: %s" % self.wordDic[self.word])
                self.guesses-=1
            else:
                updated = self.mySecretWord.update(guess)
                if not updated:
                    self.guesses-=1
            if self.guesses==0:
                notDone = False
            elif self.mySecretWord.isSolved():
                notDone = False
                won = True
        if won:
            print("You solved the puzzle!")
        else:
            print("You failed to solve the puzzle :(.")
        print("The secret word was: %s" % self.word)
            

    def chooseSecretWord(self):
        """ Chooses the secret word that will be guessed """
        return list(self.wordDic.keys())[random.randrange(len(list(self.wordDic.keys())))]
        

    def editDistance(self, s1, s2, s1Len=None, s2Len=None, memo=None):
        """ Recursively returns the total number of insertions and deletions required to convert S1 into S2 """
        #s1 is secret word (unsorted) s2 is secret word but sorted
        #compare Node value to Node value test either insert, remove, or both if unequal, else just take both out
        #make sure that if I don't have the lengths that I get them just for ease of use
        if s1Len==None and s2Len==None and memo==None:
            s1Len = s1.linkedList.length()
            s2Len = s2.linkedList.length()
            #initialize memo
            memo = []
            for i in range(s1Len):
                memo.append([])
                for j in range(s2Len):
                    memo[i].append(None)
                #print(memo[i])
        #if I ever get to a state in which one list is empty the rest of the other MUST be deleted hence len steps
        if s1Len == 0:
            return s2Len
        elif s2Len == 0:
            return s1Len        
        #memo will have memo[s1Len][s2Len] = value so I can perform quick lookups in the matrix
        #print(s1Len-1, s2Len-1)
        #print(memo[s1Len-1][s2Len-1])
        if memo[s1Len-1][s2Len-1] != None:
            return memo[s1Len-1][s2Len-1]
        
        
        #compare the head of the two, if they're the same then I incur no costs since I can freely eliminate both, however, if they're not the same I incur 2 cost
        #because I must make a replacement (deletion + insertion)
        if s1.linkedList.getHead().getData() == s2.linkedList.getHead().getData():
            cost = 0
        else:
            cost = 2
        
        #Find the minimum of all cases either by removing the front of our entered word, target word, or both
        #this creates an exponentially large amount of things to do but so long as we use decently small words it should be fine
        #(could be improved with DP) but by doing this we test every scenario, always looking for the minimum path at every step of the way
        #NOW IMPROVED WITH DP
        memo[s1Len-1][s2Len-1] = min(
            self.editDistance(s1.removeFront(), s2, s1Len-1, s2Len, memo)+1,
            self.editDistance(s1, s2.removeFront(), s1Len, s2Len-1, memo)+1,
            self.editDistance(s1.removeFront(), s2.removeFront(), s1Len-1, s2Len-1, memo) + cost)
        #for i in range(len(memo)):
            #print(memo[i])
        #print()
        return memo[s1Len-1][s2Len-1]
        
        

    def getGuess(self):
        """ Queries the user to guess a character in the secret word """
        user = input("Enter a character that has not been guessed or * for a hint: ")
        while len(user) != 1:
            print("Must enter a singular letter")
            user = input("Enter a character that has not been guessed or * for a hint: ")
        while user in self.guessed:
            print("Invalid guess. You have already guessed this letter.")
            user = input("Enter a character that has not been guessed or * for a hint: ")
        while ord(user)!=42 and (ord(user.lower())<97 or ord(user.lower())>122):
            print("Invalid guess. Must be a letter or *")
            user = input("Enter a character that has not been guessed or * for a hint: ")
        self.guessed.append(user)
        return user
            
           