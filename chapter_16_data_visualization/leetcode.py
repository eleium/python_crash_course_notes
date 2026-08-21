nums = list(input("enter a list"))
target = int(input("enter a number: "))


class Solution:
    def twoSum(self, nums, target: int):

        for x in nums:
            if  nums[y] == target-nums[x]:
                return [num[x], num[y]]
            else:
                break

s = Solution()
s.twoSum(nums, target)
