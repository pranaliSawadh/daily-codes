class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i,value in enumerate(arr):
            if(x==value):
                return i
        return -1
