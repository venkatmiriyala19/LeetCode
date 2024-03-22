class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        
        a=text.split(' ')
        c=len(a)
        print(a)
        for i in a:
            for j in i:
                if j in brokenLetters:
                    c-=1
                    break
        return c
