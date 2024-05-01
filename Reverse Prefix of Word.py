class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            b=word.index(ch)
            if (b+1!=len(word)):
                a=word[:b+1]
                word=a[::-1]+word[b+1:]
                return word
            else:
                return word[::-1]
            # print(a)
        return word
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
