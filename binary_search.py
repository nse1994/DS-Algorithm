def binary_search(list,item): # needs a sorted array 
    low = 0 
    high = len(list)-1

    while low<=high:
        mid= (low+high)//2 #find middle index of the list
        guess= list[mid]
        print(mid,guess)

        if guess==item:
            return mid
        elif guess<item:
            low = mid+1
        else:
            high=mid-1
    return None

my_list = [1,3,5,7,9,12,15,19]
print(binary_search(my_list, 15))
print(binary_search(my_list,-1))