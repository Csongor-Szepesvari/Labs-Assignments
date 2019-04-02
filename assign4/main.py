from WordGuess import WordGuess


def readWords(filename):
    """ Read in the list of possible secret words and their corresponding hints """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    dictRet = {}
    for line in lines:
        line = line.split()
        print(line)
        dictRet[line[0]] = line[1]
    return dictRet
        

def main():
    mainFlag = True
    while mainFlag:
        flag = True
        while flag:
            filename = input("Please enter a Word Guess input file: ")
            try:
                dictToPass = readWords(filename)
            except IOError:
                print("No file exists with the name %s" % filename)
            else:
                flag = False
        game = WordGuess(dictToPass)
        game.play()
        playAgain = input("Would you like to play again? (y/n): ")
        while playAgain.lower() != "y" and playAgain.lower() != "n":
            playAgain = input("Would you like to play again? (y/n): ")
        if playAgain.lower() == "n":
            mainFlag = False


if __name__ == "__main__":
    main()