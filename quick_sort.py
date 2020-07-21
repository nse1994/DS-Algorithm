def quicksort(arr):
    #base case
    if len(arr)<2:
        return arr # base case: arrays with 0 or 1 element are already "sorted"
    #inductive case 
    else:
        #pivot
        pivot = arr[0] #assume pivot is the first element 

        #sub-array less than or equal to pivot
        less = [i for i in arr[1:] if i <=pivot]

        #sub-arry greater than pivot
        greater= [i for i in arr[1:] if i >pivot]

        return quicksort(less) + [pivot]+ quicksort(greater)

print(quicksort([10,5,2,3]))


