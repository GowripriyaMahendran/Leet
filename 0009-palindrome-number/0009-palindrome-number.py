class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev = str()
        for y in x:
            rev = y +rev
        return x == rev