class Solution:
    def longestPalindrome(self,s: str)->str:
        res = s[0]
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if len(res) < r-l-1:
                res = s[l+1:r]
            
            l,r = i,i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if len(res) < r-l-1:
                res = s[l+1:r]
        return res
                

            

        