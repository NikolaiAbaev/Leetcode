def longestConsecutive(nums):
    answer = set(nums)
    top_seq = 0 

    for i in answer:
        if i - 1 not in answer:
            temp = 0
            while i in answer:
                temp += 1
                i += 1
            
            if temp > top_seq:
                top_seq = temp 
    
    return top_seq