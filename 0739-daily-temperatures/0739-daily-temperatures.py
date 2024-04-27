class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        Ans = []
        for i in range(len(temp)-1,-1,-1):
            if not stack:
                Ans.append(0)
                stack.append(i)
            else:
                if stack and temp[stack[-1]] <= temp[i]:
                    while stack and temp[stack[-1]] <= temp[i]:
                        stack.pop()
                    if stack:
                        Ans.append(stack[-1])
                        stack.append(i)
                    else:
                        Ans.append(0)
                        stack.append(i)
                elif stack and temp[stack[-1]] > temp[i]:
                    Ans.append(stack[-1])
                    stack.append(i)
        Ans.reverse()
        for i in range(len(temp)):
            if Ans[i] != 0:
                Ans[i] = abs(i - Ans[i])
        print(Ans)
        return Ans