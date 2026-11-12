class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] == nums[j]:
                return True
        return False
# Time taken: 02:14
# Not STUCK: easy, i can use a hash set too, counter too