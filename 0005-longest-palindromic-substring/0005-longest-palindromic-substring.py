class Solution:
    def longestPalindrome(self,s: str)->str:
        maxlen = 0
        string = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                output = s[i:j]

                if output == output[::-1] and len(output)>maxlen:
                    string = output
                    maxlen = len(output)
        return string

            

        