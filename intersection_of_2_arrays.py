class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))
    
# we find unique elements of both arrays using set 
# we then use intersection to get the common elements and trun it into a list