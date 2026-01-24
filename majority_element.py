class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = 0
        count = 0
        for n in nums:
            if count == 0:
                candidate = n 
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate
                
# moore voting algo (keep track of count 
# increment if canddate is same and decrement if different if count reaches 0 change candidate)
# time = o(n) space = O(1)