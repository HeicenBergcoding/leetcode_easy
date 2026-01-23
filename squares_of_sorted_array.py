class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]* len(nums)
        left = 0
        right = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left+=1
            else:
                result[i] = nums[right] ** 2
                right-=1
        return result
    
# we use 2 pointer to iterate and keep track of each element from both sides as they would be
# largest after the squares are calculated and use abs to ignore any negative or postive symbols 
# as they dont matter
# o(n) for iterating over the result array
# o(n) for storing the result array