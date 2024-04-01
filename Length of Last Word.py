class Solution(object):
    def lengthOfLastWord(self, s):
        arr=[x for x in s.split(' ')]
        for i in range(1,len(arr)+1):
            if arr[-i]=='':
                continue
            else:
                s2=arr[-i]
                return len(s2)
