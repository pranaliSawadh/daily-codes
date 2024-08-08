class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr) < 3:
            return -1
            
        arr.remove(max(arr))
        arr.remove(max(arr))
        return max(arr)

