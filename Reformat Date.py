class Solution:
    def reformatDate(self, date: str) -> str:
        Month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        a=date.split(' ')
        s=a[-1]
        b=Month.index(a[-2])
        if b+1<10:
            s+='-'+'0'+str(b+1)
        else:
            s+='-'+str(b+1)
        if int(a[-3][:-2])>=10:
            s+='-'+a[-3][:-2]
        else:
            s+='-'+'0'+a[-3][:-2]
        return s
