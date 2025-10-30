
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
        
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    s = "abc"

    print("Output is : ", sol.countSubstrings(s))
        
    s2 = "aaa"

    print("Output is : ", sol.countSubstrings(s2))
