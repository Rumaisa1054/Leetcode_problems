class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicte = {}
        for char in s:
            if char not in dicte:
                dicte[char] = 0
            dicte[char] += 1
        
        for i in range(len(s)):
            if dicte[s[i]] == 1:
                return i
        return -1