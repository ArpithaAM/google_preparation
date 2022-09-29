def find_missing_num(arr,n):
    total = ((n+1)*(n+2))/2
    sum_of_arr = sum(arr)
    return total-sum_of_arr

arr = [1, 2, 3, 5]
N = len(arr)
find_missing_num(arr,N)