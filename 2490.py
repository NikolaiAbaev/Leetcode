class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        answer = []
        counter = 0
        for i in sentence.split():
            if counter > 0:
                if i[0] == answer[-1]:
                    counter += 1
                    answer.append(i[0])
                    answer.append(i[-1:])
                else:
                    return False 
            else:
                answer.append(i[0])
                answer.append(i[-1:]) 
                counter += 1

        if answer[0] == answer[-1]:
            return True
        else:
            return False       

        