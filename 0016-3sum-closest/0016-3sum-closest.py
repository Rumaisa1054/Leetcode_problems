class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        Ans = []
        for i in range(len(nums)):
            s = i + 1
            e = len(nums)-1

            while(s<e):
                if  nums[s] + nums[e] == target - nums[i]:
                    Ans.append(target)
                    break
                elif  nums[s] + nums[e] < target - nums[i]:
                    Ans.append(nums[s] + nums[e] + nums[i])
                    s = s + 1
                     
                elif  nums[s] + nums[e] > target - nums[i]:
                    Ans.append(nums[s] + nums[e] + nums[i])
                    e = e - 1
            
        dicte = {}
        for item in Ans:
            dicte[item] = abs(item-target)
        
        mini = min(dicte.values())
        for key in dicte:
            if dicte[key] == mini:
                return key
            