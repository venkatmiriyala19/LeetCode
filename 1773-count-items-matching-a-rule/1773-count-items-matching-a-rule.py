class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        c=0
        index=0
        if ruleKey=="type":
            index=0
        elif ruleKey=="color":
            index=1
        else:
            index=2
        
        for i in items:
            if ruleValue==i[index] :
                c+=1
        return c
                
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        