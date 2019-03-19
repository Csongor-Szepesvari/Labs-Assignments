# Recursive Selection Sort Algorithm in Python 3 

import random
import time

def swap(aList, x, y):
    aList[x], aList[y] = aList[y], aList[x]

def recursive_selection_sort(array, array_len, index = 0): 
    #find the max element and put it to the index, increment index
    maxI = index
    for i in range(index, array_len):
        if array[i]>array[maxI]:
            maxI = i
    #now have maxI as the index of the largest element
    #swap
    swap(array, index, i)
    if index+1<array_len:
        recursive_selection_sort(array, array_len, index+1)
    

def iterative_selection_sort(data):
    for index in range(len(data)):
        small_index = index
    
        # finding smallest
        for i in range(index,len(data)):
            if (data[i] > data[small_index]):
                small_index=i
            
        # swapping
        temp=data[index] 
        data[index]=data[small_index]
        data[small_index]=temp
    

if  __name__== "__main__":
    # Define the list of random numbers
    array_1 = [random.randint(1,1000) for i in range(200)]
    array_2 = array_1[:]
    array_len = len(array_1) 
    sorted_list = sorted(array_1, reverse=True)
    # Calculate the execution time
    start_rec = time.time()
    recursive_selection_sort(array_1, array_len)
    end_rec = time.time()
    
    start_iter = time.time()
    iterative_selection_sort(array_2)
    end_iter = time.time()
    
    # Print the rsults
    print('The execution time:')
    print(' - Recursive selection sort: {}'.format(end_rec - start_rec))
    print(' - Iterative selection sort: {}'.format(end_iter - start_iter))





      

