class Solution:
    def sortSentence(self, s: str) -> str:
        str_list = s.split(" ")
        output = [" " for i in range(len(str_list))]
        
        for i in range(len(str_list)):
            output[int(str_list[i][-1]) - 1] = str_list[i][:-1]
        
        return " ".join(output)
        