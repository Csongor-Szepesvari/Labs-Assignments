from Node import Node

class LinkedList:
    """ The Singly-Linked List class defined in lecture """

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def add(self, item):
        temp = Node(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.size -= 1

        return found

    def append(self, item):
        temp = Node(item, None)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.size += 1

    def pop(self, i=None):
        current = self.head
        previous = None
        if i==None:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
        else:
            for j in range(i):
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size -= 1
        return current.getData()
    
    
    def getHead(self):
        return self.head
    
    def insert(self, index, item):
        assert index<=self.size, "index too large"
        if index == self.size:
            self.append(item)
        else:
            i = 0
            current = self.head
            previous = None
            while i != index:
                previous = current
                current = current.getNext()
                i += 1
            temp = Node(item, current)
            if previous !=None:
                previous.setNext(temp)
            else:
                self.head = temp
            self.size += 1
        
    def copy(self):
        copy = LinkedList()
        current = self.head
        while current != None:
            copy.append(current.getData())
            current = current.getNext()
        return copy

class SecretWord:

    def __init__(self):
        self.linkedList = LinkedList()

        # Additional attribute(s) go here:

    def setWord(self, word):
        """ Adds the characters in 'word' to self.linkedList in the given order """
        toAdd = list(word)
        for c in toAdd:
            self.linkedList.append(c)
    
    def removeFront(self):
        newWord = self.copy()
        newWord.linkedList.pop(0)
        return newWord
        
    def sort(self):
        """ Sorts the characters stored in self.linkedList in alphabetical order """
        i = 0
        #return a new secret word object
        toRet = SecretWord()
        
        while i<self.linkedList.length():
            j = 0
            placed = False
            #toCompare will be the ith element in the original list
            #it will compare itself to every jth element up to i to find its place in the linked list
            toCompare = self.linkedList.getHead()
            for h in range(i):
                toCompare = toCompare.getNext()
            current = toRet.linkedList.getHead()
            while j<toRet.linkedList.length() and not placed:
                if toCompare.getData() <= current.getData():
                    placed = True
                    toRet.linkedList.insert(j, toCompare.getData())
                else:
                    j += 1
                    current = current.getNext()
            if j == i:
                toRet.linkedList.insert(j, toCompare.getData())
            i += 1
        return toRet
                    
                    
                    
                

    def isSolved(self):
        """ Returns whether SecretWord has been solved (all letters in the word have been guessed by the user) """
        solved = True
        current = self.linkedList.getHead()
        for i in range(self.linkedList.length()):
            if not current.getDisplay():
                solved = False
                break
            current = current.getNext()
        return solved

    def update(self, guess):
        """ Updates the nodes in self.linkedList that match 'guess' """
        updated = False
        current = self.linkedList.getHead()
        while current != None:
            if current.getData() == guess:
                current.setDisplay(True)
                updated = True
            current = current.getNext()
        return updated

    def printProgress(self):
        """ Prints the current game progress
        Ex: y _ l l _ w """
        outStr = ""
        current = self.linkedList.getHead()
        while current != None:
            if current.getDisplay():
                outStr += current.getData()
            else:
                outStr += "_"
            if current.getNext() != None:
                outStr += " "
            current = current.getNext()
        return outStr
            
    def copy(self):
        newWord = SecretWord()
        newWord.setWord(str(self))
        return newWord

    def __str__(self):
        """ Converts the characters in self.linkedList into a string """
        outStr = ""
        current = self.linkedList.getHead()
        while current != None:
            outStr += current.getData()
            current = current.getNext()
        return outStr


        