class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        listSize = len(nums)
        for i in range (listSize):
            for j in range(i+1, listSize):
                if nums[i] + nums[j] == target:
                    answer = [i,j]
        return answer