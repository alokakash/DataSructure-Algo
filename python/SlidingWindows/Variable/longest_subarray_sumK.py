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

# This approach is applicable only when all numbers are positive
def max_size (arr, required_sum):
    answer, current_sum =0,0
    sum_vs_len_map = dict()
    for i in range(len(arr)):
        current_sum +=arr[i]
        if (current_sum==required_sum):
            answer = i+1
        elif(current_sum-required_sum ) in sum_vs_len_map :
            answer = max(answer, i - sum_vs_len_map[current_sum-required_sum])
        if (current_sum not in sum_vs_len_map):
            sum_vs_len_map[current_sum]=i
    
    return answer
        


arr = [4,1,1,1,2,3,1,5]
print(max_size(arr,5))
print(max_size([5,6,-5,3,2,2,1,7,-3,-4],8))

print(max_size_when_postive_no(arr,5))




