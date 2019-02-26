class Queue():
    def __init__(self):
        self.queue = []
        self.length = 0
    
    def enqueue(self, item):
        self.queue.append(item)
        self.length += 1
        
    def dequeue(self):
        if not self.isEmpty():
            self.length -= 1
            return self.queue.pop(0)
        else:
            raise Exception("Queue is already empty")
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def peek(self):
        if not self.isEmpty:
            return self.queue[0]
        else:
            raise Exception("Queue is empty")
    
    def show(self):
        print(self.queue)
        
    def __str__(self):
        return str(self.queue)

class BQueue(Queue):
    def __init__(self, capacity):
        assert type(capacity) == int, "Error: capacity must be an integer"
        assert capacity>=0, "Error: capacity must be greater than or equal to 0"
        Queue.__init__(self)
        self.capacity = capacity
    
    def isFull(self):
        return self.capacity == self.length
    
    def enqueue(self, item):
        if not self.isFull():
            self.queue.append(item)
            self.length += 1
        else:
            raise Exception("Queue is full", self.length)
        
    def capacity(self):
        return self.capacity
    
    def clear(self):
        self.length = 0
        self.queue = []
        
    def __str__(self):
        str_exp = ""
        for item in self.queue:
            str_exp += (str(item) + " ")
        return str_exp
    
    def __repr__(self):
        return str(self)+ " Max=" + str(self.capacity)
        
class CQueue(BQueue):
    def __init__(self, capacity):
        BQueue.__init__(self, capacity)
        self.head = 0
        self.tail = 0
        self.queue = [None for i in range(self.capacity)]
        
    def enqueue(self, item):
        if self.isFull():
            raise Exception("Error, queue is full", self.length)
        else:
            self.queue[self.tail] = item
            self.length += 1
            self.tail = (self.tail+1) % self.capacity
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Error, queue is already empty")
        else:
            toRet = self.queue[self.head]
            self.queue[self.head] = None
            self.length -= 1
            self.head = (self.head+1) % self.capacity
            return toRet
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Error, queue is empty")
        else:
            return self.queue[self.head]
        
    def clear(self):
        self.queue = [None for i in range(self.capacity)]
        self.length = 0
        self.head = 0
        self.tail = 0
        
    def __str__(self):
        str_exp = "]"
        i=self.head
        for j in range(self.length):
            str_exp += str(self.queue[i]) + " "
            i = (i+1)%self.capacity
        return str_exp + "]"
        
    def __repr__(self):
        return str(self.queue) + " H=" + str(self.head) + " T=" + str(self.tail) + "(" + str(self.length)+"/"+str(self.capacity)+")"
def test():
    import time as t
    numItems = 100000
    circ = CQueue(numItems)
    bounded = BQueue(numItems)
    while not bounded.isFull():
        #fill the queues up
        circ.enqueue(1)
        bounded.enqueue(1)
        
    start = t.time()
    while not circ.isEmpty():
        circ.dequeue()
    print("Circular queue took %.2f time to dequeue %d items" % (t.time()-start, numItems))
    
    start = t.time()
    while not bounded.isEmpty():
        bounded.dequeue()
    print("Bounded queue took %.2f time to dequeue %d items" % (t.time()-start, numItems))