# Given a set of time intervals in any order, merge all overlapping intervals into one and output the result 
# which should have only mutually exclusive intervals.
    

def merge_overlapping(arr):
    arr.sort() 
    index = 0
    
    for i in range(0,len(arr)):
        if(arr[index][1]>=arr[i][0]):
            arr[index][1] = max(arr[index][1],arr[i][1])
        else:
            index = index+1
            arr[index] = arr[i]
            
    for i in range(index+1):
        print(arr[i])
        
    return arr

arr =  [[6, 8], [1, 9], [2, 4], [4, 7]]
merge_overlapping(arr)
