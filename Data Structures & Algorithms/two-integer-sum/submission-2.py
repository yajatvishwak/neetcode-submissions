class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d:
                return [d[comp] ,i]
            d[nums[i]] = i
        return []

# Time taken: 3:26
# Got a little confused with what needs to be stored, then printed d and then i came to know 