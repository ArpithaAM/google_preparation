# Given an array of integers and a value, determine if there are any two integers 
# in the array whose sum is equal to the given value.

def find_sum_of_2_num(given_sum,n,arr):
   
    count = 0
    for i in range(0,n):
        for j in range(1,n):
            if ((arr[i] + arr[j]) == given_sum):
                count+=1
                print(arr[i],arr[j])

    return count

arr = [1,5,4,27,3,2] 
given_sum = 6
n = len(arr) 
find_sum_of_2_num(given_sum,n,arr)

