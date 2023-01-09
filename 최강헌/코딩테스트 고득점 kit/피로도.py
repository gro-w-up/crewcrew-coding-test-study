# k = 80
# dungeons = [[80,20],[50,40],[30,10]]
# result = 3
# 참조 : https://it-jm.tistory.com/171
# https://velog.io/@soorim_yoon/DFS%EC%99%84%EC%A0%84%ED%83%90%EC%83%89-%ED%94%BC%EB%A1%9C%EB%8F%84-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2

answer = 0


def dfs(k, dungeons, maxCount, visitedArray):
    global answer
    answer = max(answer, maxCount)

    for i in range(len(dungeons)):
        if visitedArray[i] == 0 and k >= dungeons[i][0]:
            visitedArray[i] = 1
            dfs(k - dungeons[i][1], dungeons, maxCount + 1, visitedArray)

            #백트래킹 예시  https://fomaios.tistory.com/entry/Algorithm-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9Backtracking%EC%9D%B4%EB%9E%80
            visitedArray[i] = 0


def solution(k, dungeons):
    visitedArray = [0] * len(dungeons)
    dfs(k, dungeons, 0, visitedArray)
    print(answer)
    return answer


solution(80, [[80, 20], [50, 40], [30, 10]])
