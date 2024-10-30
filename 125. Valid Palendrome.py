class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum() == True:
                string += i
        return string.lower() == string[::-1].lower()
  