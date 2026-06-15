class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force (LION METHOD #MODE)
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    if nums[i] < nums[j]:
                        return [i, j]
                    return [i, j]
        