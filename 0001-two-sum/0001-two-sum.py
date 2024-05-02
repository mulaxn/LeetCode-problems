class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        output = []

        

        #loop through all the items in the list and find which adds up to the target, if not keep searching 
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.nums[i]+self.nums[j] == self.target:
                    return [i,j]
        return []
solution = Solution()
result = solution.twoSum([3,2,4],6)
print(result)
