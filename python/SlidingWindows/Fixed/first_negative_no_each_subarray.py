# To find first negative no in each subarray of size K using Sliding windows & brute force both
# Auther: Alok Kumar Akash
from collections import deque
def first_negative_no_using_brute(arr, k):
    array_size = len(arr)
    last_negative_no_index=0
    for i in range(array_size-k+1):
        negative_checking_start=max(last_negative_no_index,i)
        for j in range (negative_checking_start, k+i): # Range can be (i, i+k)
            negative_no_found = False
            if (arr[j] <0):
                print(arr[i:k+i])
                print(arr[j])
                last_negative_no_index=j
                negative_no_found = True
                break
        if not(negative_no_found):
            print(arr[i:k+i])
            print(0)

def first_negative_no (arr, k):
    n = len(arr)
    q = deque()
    # Get -ve No in first K elements of Array
    for i in range (k):
        if (arr[i]<0):
            q.append(arr[i])

    # As -ve no from First Sub array has been appended in Queue
    # Now check in other subset also. So iterating i 
    for i in range(k,n):
        #print("i"+str(i), end =" ")
        #print(q, end = ' ')
        #print(arr[i-k:i])
        if (not q):
            print(0, end = ' ')
        else :
            print(q[0], end = ' ')
            if (arr[i-k]==q[0]):
                q.popleft()    
        if ( arr[i]<0):
            q.append(arr[i])

    if (not q):
        print(0, end = ' ')
    else :
        print(q[0])



arr = [2,3,-1,4,-5,-4,1,2,3,-9]
first_negative_no(arr,3)
#first_negative_no_using_brute(arr,3)