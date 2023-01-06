def maxSum(arr, subArraySize):
    arraySize = len(arr)
    if (arraySize<=subArraySize): 
        print("Invalid Windows")
        return -1

    # Sum of first K elements of array
    current_window_sum = sum([ arr[i] for i in range (subArraySize) ] )
    max_sum = current_window_sum 

    for i in range (arraySize - subArraySize):
        current_window_sum = current_window_sum - arr[i] + arr[i+ subArraySize]
        max_sum = max(current_window_sum,max_sum)

    return max_sum 

arr=[1,5,6,4,14,9,8,4]
print("maxSum:"+ str(maxSum(arr, 3)))  

arr = [80,-50,90,100]
k=2
answer=maxSum(arr,k)
print (answer)
