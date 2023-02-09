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

def merge(left, right)->list[int]:
    global KEY_COMPARISONS # need to implement the comparison for part (c)
    
    sorted_array = [] #using an external axuiliary array
    leftIndex,rightIndex = 0,0
    
    while (leftIndex < len(left) or rightIndex < len(right)):
        if leftIndex == len(left): #this means that the left is already all checked
            sorted_array.append(right[rightIndex]) #hence we append the right elemnt and increment the right index by 1
            rightIndex += 1
            
        elif rightIndex == len(right): #this means that the right is already all checked
            sorted_array.append(left[leftIndex]) #hence we append the left element and increment the left index by 1
            leftIndex += 1
            
        elif (left[leftIndex] < right[rightIndex]): #if the element in left is less than the right
            sorted_array.append(left[leftIndex]) #append the left element, and increment the right element
            leftIndex += 1
            KEY_COMPARISONS += 1 #update key comparisons
        else:
            sorted_array.append(right[rightIndex]); #if the element in the right is less than the left
            rightIndex += 1         # append the right element, and increment the left element
            KEY_COMPARISONS += 1 #update key comparisons
            
    return sorted_array
    

def main(): # in this particular implementation, we fix the input size of n, and vary the size of S.
    global KEY_COMPARISONS
    
    size_of_array = int(input("enter the value of N (Size of array): "))
    S = 1
    
    while S <= 15:
        KEY_COMPARISONS = 0
        #print(f"random array generated..",end="\n")
        arr = generate_random_array(size_of_array) 
        #print(arr,end="\n")
   
        #print("sorting the array...",end="\n")
        arr = hybrid_sort(arr,S)
        
        #print(f"value of S : {S}, number of key comparisons : {KEY_COMPARISONS} , size of array : {size_of_array}", end="\n" )
        table.add_row([S,size_of_array,KEY_COMPARISONS])
        
        S +=1
        
def plot_graph(table):
    X = []
    Y = []
    
    for row in table.rows:
        X.append(row[table.field_names.index("Value of S")])
        Y.append(row[table.field_names.index("Number Of Key Comparisons")])
    
    plt.plot(X,Y)
    plt.xlabel("Value of S")
    plt.ylabel("Number of Key Comparisons")

    plt.show()
        

    
        
main()
print(table)
plot_graph(table)

# comments by cheng
# suppose array size of 1000