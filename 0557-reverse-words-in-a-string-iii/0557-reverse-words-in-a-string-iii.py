class Solution:
    def reverseWords(self, s: str) -> str: 
            words = s.split(" ")
            newWords = [word[::-1] for word in words]
            
            newSentence = " ".join(newWords)

            return newSentence        