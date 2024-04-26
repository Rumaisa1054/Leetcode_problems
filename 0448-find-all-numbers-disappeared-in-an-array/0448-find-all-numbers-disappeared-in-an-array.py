class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        A = set(nums)
        Ans = []
        #1->n
        for i in range(1,len(nums)+1):
            if i in A:
                continue
            else:
                Ans.append(i)
        return Ans
                