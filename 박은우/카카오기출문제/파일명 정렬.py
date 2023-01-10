def solution(files):

    answer = []
    # 파일명 3가지 구성 선언
    head, number, tail = '', '', ''

    # 파일리스트에서 각 파일명을 가져온다.
    for file in files:
        # 가지고 온 파일명의 길이만큼 반복한다.
        for i in range(len(file)):
            # 만약, 파일명의 i번째 문자가 숫자이면
            if file[i].isdigit():
                # 파일명에서 i번째 까지는 HEAD
                head = file[:i]
                # 파일명에서 i부터 뒤까지는 NUMBER로 우선 구분
                number = file[i:]

                # number의 길이만큼 반복한다.
                for j in range(len(number)):
                    # 만약, NUMBER의 j번째의 문자가 숫자가 아니면
                    if not number[j].isdigit():
                        # J번째 부터는 TAIL
                        tail = number[j:]
                        # J번째 까지는 숫자
                        number = number[:j]
                        # 원하는 값을 얻었으니 반복문 종료
                        break

                # 디버그
                print('head = {}, number = {}, tail = {}'.format(head, number, tail))

                # 각 파일명 별로 파싱한 데이터를 배열에 추가
                answer.append([head, number, tail])
                # 다음 파일명 처리를 위해 초기화
                head, number, tail = '', '', ''
                # 끝까지 처리되지 않도록 반복문 종료
                break

    print('before sorted answer = {}'.format(answer))
    # 참고 자료 : sorted 관련 https: // ooyoung.tistory.com / 59
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    print('sorted answer = {}'.format(answer))
    answer = [''.join(i) for i in answer]
    print('result answer = {}'.format(answer))
    return answer

# 출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# 출력: ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))