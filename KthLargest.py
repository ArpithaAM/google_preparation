#Kth largest element in a stream 
#Problem Statement
#Design a class to efficiently find the Kth largest element in a stream of numbers.

class KthLargest:
    def __init__(self,k,nums):
        self.k = k
        self.nums = nums

    def add(value):
        self.nums.append(value)
        self.nums.sort()
        return self.nums[len(self.nums) - k]

kthLargest = KthLargest(2, [4,8, 2,1])
kthLargest.add(3)   # return 4
kthLargest.add(5)   # return 5
kthLargest.add(10)  # return 8
kthLargest.add(9)   # return 9
kthLargest.add(4)   # return 9