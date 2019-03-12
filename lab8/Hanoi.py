def Hanoi(number, a, b, c):
    global COUNTER
    #a b c are stacks, want to move from a to b
    #print(number)
    if number >= 1:
        #move 1 less to the third column
        Hanoi(number-1, a, c, b)
        #move the base to the second column
        #print(A,B,C)
        b.append(a.pop())
        print(A, B, C, "Times exe:", COUNTER)
        COUNTER+=1
        #now move the 1 less back to the second column
        Hanoi(number-1, c, b, a)
        #print("second")
        
        
A = []
B = []
C = []
COUNTER = 1
num = 10
for i in range(num):
    A.append(num-i)
Hanoi(num, A, B, C)
    