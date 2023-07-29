class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    ans.append(i)
                    ans.append(j)

        return ans