import numpy as np
def solution(m,n,board):
    list = []

    for i in board:
        for j in i:
            list.append(j)

    list = np.array(list).reshape(m,n)
    test = np.zeros((m, n))
    a = []

    while 1: #전체 코드 돌리는 for문

        for i in range(m):
            if i+1 != len(list):
                for j in range(1,n):
                    if list[i][j - 1]==list[i][j]==list[i + 1][j]==list[i + 1][j - 1] :
                        if list[i][j-1] == ' ' or list[i][j-1] == '':
                            test[i][j - 1], test[i][j], test[i + 1][j], test[i + 1][j - 1] = '0' * 4
                        else:
                            test[i][j-1],test[i][j],test[i+1][j],test[i+1][j-1] = '1'*4

        a.append(np.sum(test))
        r = np.sum(test)

        testwhere = np.where(test == 1)
        list[testwhere] = "@"

        for g in range(max(m,n)):
            for i in range(m):
                if i - 1 != -1:
                    for j in range(0, n):
                        if list[i][j] == '@' or list[i][j] == '':
                            if list[i-1][j] is not None:
                                list[i][j] = list[i - 1][j]
                                list[i - 1][j] = ''

        test[testwhere] = 0

        if r == 0:
            answer = sum(a)
            return answer