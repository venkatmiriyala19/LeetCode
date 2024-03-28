class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set()
        for i in sentence:
            s.add(i)
        if len(s)>=26:
            return True
        return False
