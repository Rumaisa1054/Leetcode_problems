class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # taking all unique elements
        nums_set = set(nums)
        # first missing = 1 min element that is positive
        first_missing = 1
        # if current element in set then check next positive
        while first_missing in nums_set:
            first_missing +=1
        # return the positve not in set
        return first_missing

        """ we are using set beacuse in keyword in nums has time complexity of 0(n)"""