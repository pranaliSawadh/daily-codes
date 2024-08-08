#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        count=0
        set1 = set(arr1)
        set2 = set(arr2)
        for i in arr1:
            #for j in arr2:
            #for j in arr2:
            if x-i in set2:
                count += 1
        return count

