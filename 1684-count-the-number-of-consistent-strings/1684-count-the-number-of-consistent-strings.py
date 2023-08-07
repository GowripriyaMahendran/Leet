class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=set(allowed)
        n=len(words)
        for i in words:
            for c in i:
                if c not in ans:
                    n-=1
                    break
        return n
        