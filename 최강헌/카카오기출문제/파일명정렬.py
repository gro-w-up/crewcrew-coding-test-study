'''
1. HEAD , NUMBER, TAIL 분리

'''


def solution(files):
    answer = []

    for j in files:
        head, number, tail = "", "", ""
        startNumber = False

        for i in range(len(j)):
            if j[i].isdigit():
                number += j[i]
                startNumber = True
            elif not startNumber:
                head += j[i]
            else:
                tail = j[i:]
                break

        answer.append((head, number, tail))

    '''
    #이곳에서 어려움이 있었음
    #sort : 원본을 변형시켜 정렬
    sorted 정렬된 결과를 반환하여 원형 변경 x
    여기서 사용한 lambda key 를 통하여 정렬 할수 있음
    따라서 파일명으로 한번 정렬 후, 숫자로 정렬한다
    '''
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))

    return [''.join(t) for t in answer]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
