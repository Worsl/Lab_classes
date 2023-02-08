import random
import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

KEY_COMPARISONS = 0
records = {}
table = PrettyTable()
table.field_names = ["Value of S", "Size of array (N)","Number Of Key Comparisons"]

def generate_random_array(size_of_array):
    arr = []
    for _ in range(0,size_of_array+1):
        arr.append(random.randint(1,size_of_array))
    return arr

def hybrid_sort(arr, S:int): #returns an array sorted
    length = len(arr)
    
    if length <= S: #base case to enter insertion sort
        sorted = insertion_sort(arr)
        return sorted
    
    mid = length//2
    left_subarray = arr[:mid] #uptill and exclusive of mid index
    right_subarray = arr[mid:] #from mid index inclusive, to the end.
    
    left = hybrid_sort(left_subarray,S)
    right = hybrid_sort(right_subarray,S)


    return merge(left,right)    
  
def insertion_sort(arr):
    global KEY_COMPARISONS
    length = len(arr)
    for i in range(1, length):
        for j in range(i,0,-1):
            KEY_COMPARISONS += 1
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1] #Python swap syntax
            else:
                break
    return arr

def merge(left, right):
    global KEY_COMPARISONS # need to implement the comparison for part (c)
    
    sorted_array = [] #using an external axuiliary array
    leftIndex,rightIndex = 0,0
    
    while (leftIndex < len(left) or rightIndex < len(right)):
        if leftIndex == len(left):
            sorted_array.append(right[rightIndex]);
            rightIndex += 1
        elif rightIndex == len(right):
            sorted_array.append(left[leftIndex])
            leftIndex += 1
            
        elif (left[leftIndex] < right[rightIndex]):
            sorted_array.append(left[leftIndex])
            leftIndex += 1
            KEY_COMPARISONS += 1
        else:
            sorted_array.append(right[rightIndex]);
            rightIndex += 1
            KEY_COMPARISONS += 1
            
    return sorted_array
    
def pause():
    time.sleep(1)

def main():
    global KEY_COMPARISONS
    
    S = int(input("enter value of S: "))
    size_of_array = 100
    
    while size_of_array <= 10000:
        KEY_COMPARISONS = 0
        #print(f"random array generated..",end="\n")
        arr = generate_random_array(size_of_array) 
        #print(arr,end="\n")
   
        #print("sorting the array...",end="\n")
        arr = hybrid_sort(arr,S)

        
        # print(f"value of S : {S}, number of key comparisons : {KEY_COMPARISONS} , size of array : {size_of_array}", end="\n" )
        table.add_row([S,size_of_array,KEY_COMPARISONS])
        
        size_of_array *=2
        
def plot_graph(table):
    X = []
    Y = []
    
    for row in table.rows:
        X.append(row[table.field_names.index("Size of array (N)")])
        Y.append(row[table.field_names.index("Number Of Key Comparisons")])
    
    plt.plot(X,Y)
    plt.show()
        

    
        
main()
print(table)
plot_graph(table)


# obeservations from cheng - changing frequency of the x-axis causes a wave like property, not sure why.