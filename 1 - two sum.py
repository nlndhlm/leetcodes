# accepted solution to problem 1 - two sum (easy)

nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]


#print(Solution.twoSum(None, nums, target))
