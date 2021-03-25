import random, time

def bubbleSort(arr):
    # geekforgeeks.org bubble sorting algorithim
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def prefixSum(n):
    # Calculates prefix sum
    # Parameters:
    #   n (iterable data type)

    total = 0
    for keys in n:
        n[keys] += total
        total = n[keys]
    return n

def sort(n, col=1):
    # Sorts integers using radix sorting method. 
    # Parameters:
    #       n (iterable data type)
    #       col (current place value)

    if col == 1000: return n 
    newList = [0] * len(n) # makes new list of n length
    digits = {0:0 , 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    
    for numbers in n: 
        digits[(numbers//col) % 10] += 1
        # Calculates place value and adds to dictionary
    digits = prefixSum(digits)

    for values in n[::-1]:
        index = digits[(values//col) % 10] - 1
        digits[(values//col) % 10] -= 1
        newList[index] = values
        # Finds index from prefix sum and adds to new list

    col *= 10
    # Updates current place value spot
    return sort(newList, col)


timer = time.time()

# ----------------------------------------------------------------------------
#                               Test List
# ranList = [277,806,681,462,787,163,284,166,905,518,263,395,988,307,779,721]
# ----------------------------------------------------------------------------

ranList = [random.randint(0,999) for x in range(1,10000)]
radix = sort(ranList)

print(f"Radix Sorting took : {time.time() - timer} seconds")
print("-" * 50)

timer = time.time()
bubble = bubbleSort(ranList)
print(f"Bubble Sorting took : {time.time() - timer} seconds")
