import random
import time

comparisons = 0

def generate_random_array(lower_limit, upper_limit):
    arr = []
    size = random.randint(lower_limit, upper_limit)
    for _ in range(0,size):
        arr.append(random.randint(1,upper_limit))
    return arr

def hybrid_sort(arr, S:int):
    length = len(arr)
    
    if length <= S: #base case to enter insertion sort
        sorted = insertion_sort(arr)
        return sorted
    
    mid = length//2
    left = arr[:mid]
    right = arr[mid:]
    
    hybrid_sort(left, S)
    hybrid_sort(right, S)
    merge(left, right, arr)
    
def insertion_sort(arr):
    global comparisons
    length = len(arr)
    for i in range(1, length):
        for j in range(i,0,-1):
            comparisons += 1
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1] #Python swap syntax
            else:
                break
    return arr

def merge(left, right, arr):
    global comparisons
    
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def pause():
    time.sleep(1)


def main():
    i = 5
    while (i > 0):
        print("random array generated..")
        arr = generate_random_array(5,100)
        print(arr)
        
        pause()
        print("sorting the array...")
        pause()
        hybrid_sort(arr,7)
        print(arr,end='\n')
        
        print()
        pause()
        
        i -= 1
        
main()