from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        
        for n in nums2:
            if counts[n] > 0:
                result.append(n)
                counts[n]-=1
        return result
            
# we create a hashmap for keeping the counts of 1st array
# we check for occurences based on counts from second array
# keep the values that intersect even the duplciates decrementing the counter as values appear

# time_complexity O(n) for first iteration of array over counter and 
# 2nd when we iterate over the second array so 0(m+n)
# Auxilary space - O(n) as we store the counts of n keys
# Output space - O(min(n,m)) as it has to have the number of elements in the 
# smaller array in the worst case scenario