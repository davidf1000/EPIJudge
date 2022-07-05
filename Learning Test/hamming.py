class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = (x^y)
        sum = 0 
        while res!=0:
            if(res&1==1):
                sum+=1
            res >>=1
        return sum

Sol = Solution()
print(Sol.hammingDistance(1,4))