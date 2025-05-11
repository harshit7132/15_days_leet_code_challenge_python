class Solution(object):
    def twoSum(self, nums, target):
        # Loop through the list of numbers
        for i in range(len(nums)):
            # For each number, loop through the remaining numbers (starting from the next index)
            for j in range(i+1, len(nums)):
                # Check if the sum of the two numbers equals the target
                if nums[i] + nums[j] == target:
                    # If they do, return the indices of those two numbers as a list
                    unique_index = [i, j]
                    return unique_index
