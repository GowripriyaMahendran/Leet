class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split()
        string=""
        for i in range(0,k-1):
            string+=words[i]+" "
        string+=words[k-1]
        return string
        