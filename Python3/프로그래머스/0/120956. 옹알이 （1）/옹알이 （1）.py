def solution(babbling):
    answer = 0
    str_list = ["aya", "ye", "woo", "ma"]
    
    for words in babbling:
        temp = words
        for substr in str_list:
            temp = temp.replace(substr, " ")
        if temp.replace(" ", "") == "":
            answer += 1
            
    return answer