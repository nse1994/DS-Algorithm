
""" 
https://stackoverflow.com/questions/12711397/python-recursive-function-to-find-the-largest-number-in-the-list
"""

def recursive_max(list):
    if len(lst) == 0:
        return None
    if len(list)==1:
        return list[0]
    sub_max= recursive_max(list[1:])
    return list[0] if list[0]>sub_max else sub_max  

print (recursive_max([ 5,10,20,11,3]))

# #alternate way for recursion
# def Max(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         m = Max(list[1:])
#         return m if m > list[0] else list[0]
        
# print(max([ 5,10,20,11,3]))

##alternate way for recursion
# def find_max_recursively(S, n):                                                
#     """Find the maximum element in a sequence S, of n elements."""             
#     if n == 1:  # reached the left most item                                   
#         return S[n-1]                                                          
#     else:                                                                      
#         previous = find_max_recursively(S, n-1)                                
#         current = S[n-1]                                                       
#         if previous > current:                                                 
#             return previous                                                    
#         else:                                                                  
#             return current                                                     


# if __name__ == '__main__':                                                     
#     print(find_max_recursively([5, 10, 20, 11, 3], 5)) 


