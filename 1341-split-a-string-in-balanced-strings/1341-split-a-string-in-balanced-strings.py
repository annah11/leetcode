class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in s:
            if i == "R":
                cnt +=1
            else:
                cnt -=1
            if cnt ==0:
                ans +=1
        return ans