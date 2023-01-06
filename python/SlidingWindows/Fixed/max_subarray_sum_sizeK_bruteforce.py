from math import inf
maxint=inf
# To find maximum sum of continous subarray of size K using Brute Force
# Auther - Alok  Kumar  Akash
def max_subarray_sum(arr,k):
    max_sum = -maxint -1 
    for i in range (0,len(arr)-k+1 ):
            current_sum =0
            for j in range (i,i+k):
                current_sum += arr[j]

            max_sum= max(max_sum,current_sum)

    return max_sum

def maxSubArraySum(a,size):
      
    max_so_far = -maxint - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    return max_so_far

arr=[1,5,6,4,14,9,8,4]

print(max_subarray_sum(arr, 2))
         

    
