# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))





# 내가 한거
def solution(array, commands):
    answer = []
    for i in range(0,len(commands)):
        copy=array[commands[i][0]-1:commands[i][1]]
        copy.sort()
        # print(copy)
        # print(commands[i][2])
        answer.append(copy[commands[i][2]-1])
    return answer

    
#  다른 사람 


def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
    
def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        if i == j:
            answer.append(array[i-1])
            continue

        n = array[i-1:j]
        n.sort()

        result = n[k-1]
        answer.append(result)

    return answer