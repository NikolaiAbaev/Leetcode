class Solution:
    def makeFancyString(self, s: str) -> str:
        counter = 1 
        answer = ""
        answer += s[0]

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                counter += 1
                if counter >= 3:
                    pass
                else:
                    answer += s[i]
            else:
                counter = 1
                answer += s[i]

        return answer
