class Solution(object):
    def sortVowels(self, s):
        s1=''
        s2=''
        arr=[]
        for i in range(len(s)):
            if s[i] in 'AEIOU':
                s1+=s[i]
                arr.append(i)
            if s[i] in 'aeiou':
                s2+=s[i]
                arr.append(i)
        s1_list=sorted(s1)
        s2_list=sorted(s2)
        s3=s1_list+s2_list
        for i in range(len(arr)):
            s=s[:arr[i]]+s3[i]+s[arr[i]+1:]
        return s

        
        """
        :type s: str
        :rtype: str
        """
  
