class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        hours=[8,4,2,1]
        minutes=[32,16,8,4,2,1]
        
        def backtrack(idx,leds,h,m):
            if h>11 or m>59:
                return
            if leds==turnedOn:
                res.append(str(h) + ":" + (str(m) if m >= 10 else "0" + str(m)))
                return
            for i in range(idx,10):
                if i<4:
                    backtrack(i + 1, leds + 1, h + hours[i], m)
                else:
                    backtrack(i + 1, leds + 1, h, m + minutes[i - 4])
        backtrack(0,0,0,0)       
        return res     
        



