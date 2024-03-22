class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        a=[]
        for i in words:
            s=i.split(separator)
            for j in s:
                if j!='':
                    a.append(j)
            # a.append(s)
        return a
        
