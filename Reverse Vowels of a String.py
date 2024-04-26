class Solution(object):
    def reverseVowels(self, s):
        vowel=''
        for i in s:
            if i in 'aeiouAEIOU':
                vowel+=i
        # vowel=vowel[::-1]
        s1=''
        for i in s:
            if i in 'aeiouAEIOU':
                s1+=vowel[-1]
                vowel=vowel[:-1]
                continue
            s1+=i
        return s1
