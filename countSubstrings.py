
# 647. Palindromic Substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        # l = 0
        # r = 1
        # res = 0
        # for i in range(l, len(s)):
        #     for j in range(r, len(s)+1):
        #         string = s[i:j]
        #         if(string == string[::-1]):
        #             res += 1
        #             l += 1
        #
        #     r += 1
        #
        # return res
