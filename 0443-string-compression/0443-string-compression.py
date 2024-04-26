class Solution:
    def compress(self, chars: List[str]) -> int:
        Ans = ""
        i = 0
        while i < (len(chars)):
            Ans = Ans + (chars[i])
            count = 1
            j = i + 1
            while j < (len(chars)):
                if chars[i] == chars[j]:
                    count += 1
                    j = j + 1
                else:
                    break
            i = j
            if count != 1:
                Ans = Ans + (str(count))
            print(Ans)

        chars[:len(Ans)] = list(Ans)
        return len(Ans)
        