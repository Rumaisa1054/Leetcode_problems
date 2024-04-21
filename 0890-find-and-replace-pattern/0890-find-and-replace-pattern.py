def diction(string):
    dicte = {}
    for i in range(len(string)):
        if string[i] not in dicte:
            dicte[string[i]] = []
        dicte[string[i]].append(i)
    return dicte
class Solution:
    def findAndReplacePattern(self, word: List[str], pattern: str) -> List[str]:
        dicte = diction(pattern)
        Ans = []
        for i in range(len(word)):
            if len(set(word[i])) == len(set(pattern)):
                dicte1 = diction(word[i])
                if list(dicte.values()) == list(dicte1.values()):
                    Ans.append(word[i])
        return Ans