
def count_list(arr):
    # base case
    if arr==[]:
        return 0
    # recursive case
    return 1+ count_list(arr[1:])
  

print(count_list([ 1, 2, 3, 4, 5, 6]))
