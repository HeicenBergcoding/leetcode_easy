class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# we calculate the actual sum of the array using sum of naural numbers
# subtract it with actual sum to get the missing number 
# o(n) time complexity as sum fucntion iterate over the nums
# o(1) because we use only constant extra variables