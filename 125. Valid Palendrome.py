class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if self.alphaNum(s[l]) == False:
                l += 1
            elif self.alphaNum(s[r]) == False:
                r -= 1

            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1 
                    if l == r or l > r:
                        return True
                else: 
                    return False
        return True



    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))


test_s="No lemon, no melon"
solution_instance = Solution()
result = solution_instance.isPalindrome(test_s)
print(result)