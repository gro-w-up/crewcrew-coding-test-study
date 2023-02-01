import sys
sys.setrecursionlimit(10**6) # 재귀 함수 제한 해제

def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def quard(x, y, n):
        print('x = {}, y = {}, n = {}, arr[x][y] = {}'.format(x, y, n, arr[x][y]))
        first = arr[x][y]

        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != first:
                    n = n // 2
                    quard(x, y, n)
                    quard(x, y + n, n)
                    quard(x + n, y, n)
                    quard(x + n, y + n, n)
                    return

    quard(0, 0, n)

    return (answer)

# Expect [4, 9]
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# Expect [10, 15]
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))