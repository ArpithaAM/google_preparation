# Given a sorted array, two integerskandx, 
# find thekclosest elements toxin the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
def sorted_array(arr):
    n = len(arr)
    swapped = False
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    return arr


def findCrossOver(sort_arr,k,x):
    left = 0
    right = len(sort_arr)-k
    
    while(left<right):
        mid = left+(right-left)//2
        
        if(x-sort_arr[mid]<sort_arr[mid+k]-x):
            left = mid+1
        else:
            right = mid
            
    return sort_arr[left:left+k]

arr = [1,2,3,4,5]
k=4
x=-1

########sorted array ###########
arr = sorted_array(arr)

######### find kth closet elements #############
findCrossOver(arr, x, k)
