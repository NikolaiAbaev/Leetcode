strs = ["eat","tea","tan","ate","nat","bat"]
answer_dict = {}


for words in strs:
    temp_count = [0] * 26
    for letters in words:
        temp_count[ord(letters) - ord('a')] += 1
    
    if tuple(temp_count) in answer_dict:
        answer_dict[tuple(temp_count)].append(words)
    else:
        answer_dict[tuple(temp_count)] = [words]

print(list(answer_dict.values()))