def solution(message, spoiler_ranges):
    spoiled_set = set()
    basic_set = set()
    idx = [i for i in range(len(message))]

    for start, end in spoiler_ranges:
        head = start
        tail = end

        while True:
            if head == 0:
                break
            if message[head] == " ":
                head += 1
                break
            head -= 1

        while True:
            if message[tail] == " ":
                break
            tail += 1
            if tail >= len(message):
                break

        spoiled_set.update(message[head:tail].split())

        for i in range(head, tail):
            idx[i] = -1
            
    basic_message = ""

    for i in idx:
        if i == -1:
            basic_message += " "
        else:
            basic_message += message[i]

    basic_set.update(basic_message.split())

    return len(spoiled_set - basic_set)