# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        if n==1:
            return 0
        for i in range(n):
            #if i is not None and (i < 0 or i >= n):
            if n>1 and i == 0:
                if arr[i] >= arr[i+1]:
                    return i
            # For the last element, only compare with the previous element
            elif i == n-1:
                if arr[i] >= arr[i-1]:
                    return i
            else:
                if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
                    return i

