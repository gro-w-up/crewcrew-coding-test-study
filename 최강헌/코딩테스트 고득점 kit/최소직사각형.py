'''
풀이 및 접근방법
1. 모든 배열 순회하며 가장 큰 것을 가로로 놓기
2. 가로, 세로 가장큰 것 갖고오기
'''


def solution(sizes):
    widthList = list()
    heightList = list()

    for w, h in sizes:
        maxSize = max(w, h)
        minSize = min(w, h)
        widthList.append(maxSize)
        heightList.append(minSize)

    return max(widthList)*max(heightList)




print('result 1 : ', solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
