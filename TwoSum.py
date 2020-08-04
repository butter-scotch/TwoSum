class Solution:
  def twoSum(self, nums, target):

    h = {}
    for i, num in enumerate(nums):
      n = target - num
      if n not in h:
        h[num] = i
      else:
        return [h[n], i]
      

result = Solution()
print(result.twoSum([2, 7, 11, 15], 9))

# h(hash table) = {
#   [0, 2]
# }

# i = 0, 1
# num = 2, 7
# n = 7, 2