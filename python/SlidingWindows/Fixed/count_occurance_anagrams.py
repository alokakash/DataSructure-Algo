# To find count of anagram in text  using Sliding windows & brute force both
# Auther: Alok Kumar Akash

def find_count(text,pattern):
    count_dict = {}
    ans=0
    k = len(pattern)
    for letters in pattern:
        count_dict[letters] = count_dict.get(letters, 0) + 1
    unique_chracters_left = len(count_dict)

    #1. Check first window
    for keys in text[:k]:
        no_of_occ = count_dict.get(keys)
        if(no_of_occ is not None):
            count_dict[keys]= no_of_occ - 1
            if(no_of_occ==1):
                unique_chracters_left -=  1

    for i in range (k ,len(text)):
        if(unique_chracters_left==0):
            ans += 1
        old_letter= text[i-k]
        no_of_occ = count_dict.get(old_letter)
        if(no_of_occ is not None):
            count_dict[old_letter] = no_of_occ + 1
            if(no_of_occ==0):
                unique_chracters_left +=  1

        new_letter= text[i]
        new_occ = count_dict.get(new_letter)
        if(new_occ is not None):
            count_dict[new_letter] = new_occ - 1
            if(new_occ==1):
                unique_chracters_left -=  1
    if (unique_chracters_left==0):
        ans +=1

    print(ans)    

        
        



text="forxxorfxdofr"
p="for"
find_count(text,p)    