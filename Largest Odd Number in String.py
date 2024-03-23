class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(1,len(num)+1):
            # print(num[-i])
            if num[-i] in '02468':
                continue
            return num[:-i]+num[-i]
        return ''
