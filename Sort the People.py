class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=[]
        a[:]=heights
        a.sort()
        a=a[::-1]
        c=[]
        for i in a:
            b=heights.index(i)
            # print(name)
            c.append(names[b])
        return c


        
