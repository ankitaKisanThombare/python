'''The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.'''

def maxSequence(arr):
    l=[]
    for i in range(len(arr)):
        n=i
        sum1=0
       
        while(n<len(arr)):
            sum1=sum1+arr[n]
            l.append(arr[i:n])
            n=n+1
    
    max1=0
    res=[]
    
    for i in l:
        sum2=0
        for j in i:
            sum2=sum2+j
        if sum2>max1:
            max1=sum2
            res=i
    return res
        
print(maxSequence([-2, 1, -3, 4, -5, 2, 1, -5, 4]))
       
    
    
