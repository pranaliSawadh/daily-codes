
def isSubset( a1, a2, n, m):
      
    for i in a2:
        if a2.count(i)<=a1.count(i):
            if i not in a1:
                return "No"
        else:
            return "No"
    return "Yes"
