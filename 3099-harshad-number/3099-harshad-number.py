class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        st = str(x)
        s = 0
        for i in st:
            s = s + int(i)
        if x%s == 0:
            return s
        else:
            return -1