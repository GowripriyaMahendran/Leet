class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        tcount = 0
        for i in nums:
            count = 0
            while i>0:
                count +=1
                i =i//10
            if count % 2==0:
                tcount+=1
        return tcount        
            
        