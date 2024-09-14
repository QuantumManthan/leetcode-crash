class Solution:
    def twoSum(self, nums, target):
        sum = 0
        counter = 0
        while sum < target:
            sum = nums[counter] + nums[counter + 1]
            if sum != target:
                sum = 0
            else:
                result = [nums.index(nums[counter]), nums.index(nums[counter + 1])]
                print(result)
            counter += 1
        return sum


obj = Solution()
print(obj.twoSum([3, 2, 4], 6))
print(obj.twoSum([2, 7, 11, 5], 9))
print(obj.twoSum([3, 3], 6))

