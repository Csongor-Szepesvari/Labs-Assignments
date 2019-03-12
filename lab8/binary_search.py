def binarySearch (listNumbers, low, high, key):
    if low > high or high < low:
        return -1
    index = low + (high-low)//2
    result = listNumbers[index]
    #print(index, result, low, high, key)
    if result == key:
        return index
    elif result < key:
        return binarySearch(listNumbers, index + 1, high, key)
    else:
        return binarySearch(listNumbers, low, index - 1, key)


# Test array 
def main():
    array_for_test = [-8,-2,1,3,5,7,9]
    print(binarySearch(array_for_test,0,len(array_for_test)-1,9))
    print(binarySearch(array_for_test,0,len(array_for_test)-1,-8))
    print(binarySearch(array_for_test,0,len(array_for_test)-1,4))
    
main()