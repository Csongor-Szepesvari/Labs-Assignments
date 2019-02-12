def readAccounts(infile):
    myDict = {}
    for line in infile.readlines():
        try:
            cur = line.split(":")
            cur[1] = float(cur[1])
        except ValueError:
            print("Value Error. Account for %s not added: illegal value for the balance" % cur[0])
        else:
            myDict[cur[0]] = cur[1]
    return myDict
        
def processAccounts(accounts):
    mainFlag = True
    while mainFlag:
        flag = True
        while flag:
            try:
                name = input("Enter an account name or 'Stop' to exit: ")
                if name != "Stop":
                    accounts[name]
            except KeyError:
                print("Key Error. Account for %s does not exist. Transaction cancelled" % name)
            else:
                flag = False
                if name == "Stop":
                    mainFlag = False
                else:
                    try:
                        amount = float(input("Enter a transaction amount for %s: " % name))
                    except ValueError:
                        print("Value Error. Incorrect Amount. Transaction cancelled.")
                    else:
                        accounts[name] += amount
                        print("New balance for %s is %.2f" % (name, accounts[name]))
    
def main():
    flag = True
    while flag:
        try:
            filename = input("Please enter the filename >")
            file = open(filename, 'r')
        except IOError:
            print("I/O Error: %s does not exist." % filename)
        else:
            aDict = readAccounts(file)
            flag = False
            file.close()
    processAccounts(aDict)

main()