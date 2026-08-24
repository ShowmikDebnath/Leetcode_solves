from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2

        hashmap = Counter(nums)

        for key in hashmap:
            if hashmap[key] > n:
                return key


