from d_linked_node import d_linked_node

class d_linked_list():
    
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        

            
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # adds a new item to the front of the list
        newNode = d_linked_node(item, self.__head, None)
        #print(item)
        #if empty list
        if self.__tail == None:
            self.__tail = newNode
        #print("got here")
        self.__head = newNode
        self.__size += 1
        
    def remove(self, item):
        # remove first element that is equal to the item, if it doesn't exist, nothing changes
        if self.__head != None:
            #if list exists
            current = self.__head
            found = False
            #loop through to the end unless it is found
            while current != None and not found:
                if current.getData() == item:
                    found = True
                    #we've found it, now remove it
                    if current.getPrevious()!=None:
                        current.getPrevious().setNext(current.getNext())
                    else:
                        self.__head = current.getNext()
                    if current.getNext()!=None:
                        current.getNext().setPrevious(current.getPrevious())
                    else:
                        self.__tail = current.getPrevious()
                    self.__size -= 1
                else:
                    current = current.getNext()
        
    def append(self, item):
        # adds item to the end of the list
        newNode = d_linked_node(item, None, self.__tail)
        # if empty list
        if self.__head == None:
            self.__head = newNode
        self.__tail = newNode
        self.__size += 1
            
        
    def insert(self, pos, item):
        assert pos<self.__size, "Out of bounds, must be between 0-list size (exclusive)"
        assert pos>=0, "Out of bounds, must be between 0-list size (exclusive)"
        # Add item to the given position in the list (i.e if pos is 0 then item goes to the beginning of the list)
        current = self.__head
        #loop to the position to insert in
        for i in range(pos):
            current = current.getNext()
        #current = the one to go to and push back
        newNode = d_linked_node(item, current, current.getPrevious())
        if pos == 0:
            self.__head = newNode
        elif pos == self.__size:
            self.__tail = newNode
        self.__size += 1
        
        
    def pop(self, pos=None):
        # This function gets an optional argument for position
        # o If the position has been given, removes and returns the item in the given position
        # o If the position has the default value(None), removes and returns the last item in the list
        # handle pos=None case first
        if self.__head==None or self.__tail==None:
            #handle empty case
            return None
        elif pos==None or pos==self.__size-1:
            #case with last
            #print("in here")
            toRet = self.__tail.getData()
            #print(self.__tail.getData())
            self.__tail = self.__tail.getPrevious()
            self.__size -= 1
            if self.__size != 0:
                self.__tail.setNext(None)
                
            return toRet
        else:
            #position is given, test it
            assert pos<self.__size, "Out of bounds, must be between 0-list size (exclusive)"
            assert pos>=0, "Out of bounds, must be between 0-list size (exclusive)"
            current = self.__head
            for i in range(pos):
                current = current.getNext()
            #now have the correct current on the position
            toRet = current.getData()
            previous = current.getPrevious()
            if previous!=None:
                previous.setNext(current.getNext())
            else:
                self.__head = current.getNext()
            current.getNext().setPrevious(previous)
            self.__size -= 1
            return toRet
        
    def search_larger(self, item):
        # Returns the position of the first item that is larger than item, -1 if there is no item larger
        if self.__size == 0:
            return -1
        else:
            pos = 0
            current = self.__head
            while current!=None and current.getData()<=item:
                pos += 1
                current = current.getNext()
            if current==None:
                return -1
            else:
                return pos
        
    def get_size(self):
        # returns size of the list
        return self.__size  
    
    def get_item(self, pos):
        #o returns item that exists at pos, raises exception if pos doesnt exist
        #o pos can be negative which means the position from the end of the list. (-1 is the last item, -2 the second from last etc.)   
        #position is given, test it
        assert pos<self.__size, "Out of bounds, must be between -list size to list size (inclusive, exclusive)"
        assert pos>=-self.__size, "Out of bounds, must be between -list size to list size (inclusive, exclusive)"
        assert self.__size>0, "Error: List is empty"
        if pos < 0:
            current = self.__tail
            for i in range(abs(pos)-1):
                current = current.getPrevious()
            return current.getData()
        else:
            current = self.__head
            for i in range(pos):
                current = current.getNext()
            return current.getData()
        
    def __str__(self):
        # Returns a string that is the elements of the DLinkedList with spaces in between
        output = ""
        current = self.__head
        while current != None:
            output += str(current.getData())
            if current.getNext() != None:
                output += " "
            current = current.getNext()
        return output
        

def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
    #print("pass1")
            
    linked_list.add("World")
    linked_list.add("Hello")
    #print(linked_list)
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    output = linked_list.pop(1)
    is_pass = (output == "World")
    assert is_pass == True, "fail the test"     
            
    #print("Linked list (should be just hello):", linked_list)
    output = linked_list.pop()
    #print(output)
    is_pass = (output == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    #print(int_list2)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                    
        
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! You have finished exercise 1! ============")
        
#test()