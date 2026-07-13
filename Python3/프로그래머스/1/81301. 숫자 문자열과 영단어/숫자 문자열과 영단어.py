def solution(s):
    numset = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    num = {'0','1','2','3','4','5','6','7','8','9'}
    tmp = 0
    ans = '0'
    for i in range(0, len(s)):
        if s[i] not in num:
            if s[tmp:i+1] in numset.keys():
                ans += numset[s[tmp:i+1]]
                tmp = i + 1
        else:
            ans += s[i]
            tmp = i + 1

    return int(ans[1:])