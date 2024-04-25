def hasmap(stri):
    dicte = {}
    for i in range(len(stri)):
        if stri[i] not in dicte:
            dicte[stri[i]] = 0
        dicte[stri[i]] += 1
    return dicte
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dicte1 = hasmap(ransomNote)
        dicte2 = hasmap(magazine)
        for i in range(len(ransomNote)):
            if ((ransomNote[i]) in dicte2) and dicte1[ransomNote[i]] <= dicte2[ransomNote[i]]:
                continue
            else:
                return False
        return True