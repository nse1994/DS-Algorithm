#Not a very fast sorting algorithm but very neat

#Selection sort is similar to a functioned used for finding smallest in an array
def findSmallest(arr):
    smallest= arr[0] # stores the smallest value
    smallest_index= 0 # Stores the index of the smallest value
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest= arr[i]
            smallest_index =i
    return smallest_index

def selectionSort(arr): # sorts an array 
    newArr= []
    for i in range(len(arr)):
        smallest= findSmallest(arr) # Finds the smallest in the array and this will later be added into the new array
        newArr.append(arr.pop(smallest)) # pop() method returns the item present at the given index.
    return (newArr)
    
print(selectionSort([5,3,6,2,10]))

