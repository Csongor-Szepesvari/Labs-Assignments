import queuesADT as queues
flag = True
qLen = 3
vipQ = queues.CQueue(qLen)
normQ = queues.CQueue(qLen)
while flag:
    response = ""
    
    while response != "add" and response != "next" and response != "exit":
        response = input("Do you want to add a customer to the queue, serve the next customer in the queue, or exit?(add/next/exit): ")
        
    if response == "add":
        name = input("Enter the name of the person to add: ")
        VIP = input("Is the customer VIP?(y/n): ")
        if VIP == "y":
            try:
                vipQ.enqueue(name)
            except Exception:
                print("Error: VIP customers queue is full")
                error = True
            else:
                print("Add %s to VIP line." % name)
                print("Normal customers queue:", normQ)
                print("VIP customers queue:", vipQ)
                print()
                
        elif VIP == "n":
            try:
                normQ.enqueue(name)
            except Exception:
                print("Error: normal customers queue is full")
                error = True
            else:
                print("Add %s to normal line." % name)
                print("Normal customers queue:", normQ)
                print("VIP customers queue:", vipQ) 
                print()
            
    elif response == "next":
        if vipQ.isEmpty() and normQ.isEmpty():
            print("Error: Queues are empty")
        else:
            if not vipQ.isEmpty():
                name = vipQ.dequeue()
            else:
                name = normQ.dequeue()
            print("%s has been served." % name)
            print("Normal customers queue:", normQ)
            print("VIP customers queue:", vipQ)
            print()
            
    elif response == "exit":
        flag = False
            
            
        
        