# To find maximum size of continous subarray of sum K using variable Sliding windows. 
# Auther: Alok Kumar Akash

# This approach is applicable only when all numbers are positive
def max_size_when_postive_no (arr, required_sum):
    answer, current_sum,i,j = 0,0,0,0
    
    while (j<len(arr)):
        current_sum += arr[j]
        if (current_sum <required_sum):
            j+=1

        elif(current_sum==required_sum):
            answer = max(answer,j-i+1)
            j+=1
        elif (current_sum > required_sum):
            while (current_sum>required_sum):
                current_sum -= arr[i]
                i+=1
            if (current_sum==required_sum):
                answer=max(answer,j-i+1)

            j+=1
    return answer

arr = [4,1,1,1,2,3,1,5]
print(max_size_when_postive_no(arr,5))




