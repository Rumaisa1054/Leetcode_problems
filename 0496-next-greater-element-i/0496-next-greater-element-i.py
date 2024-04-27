class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        Next_great = []
        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                stack.append(nums2[i])
                Next_great.append(-1)
            else:
                if stack[-1] <= nums2[i]:
                    while stack and stack[-1] <= nums2[i]:
                        stack.pop()
                    if stack:
                        Next_great.append(stack[-1])
                        stack.append(nums2[i])
                    else:
                        stack.append(nums2[i])
                        Next_great.append(-1)
                elif nums2[i] < stack[-1]:
                    Next_great.append(stack[-1])
                    stack.append(nums2[i])
        print(Next_great)
        Next_great.reverse()
        Ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    Ans.append(Next_great[j])
        print(Ans)
        return Ans