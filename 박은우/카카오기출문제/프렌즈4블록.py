def solution(m, n, board):
    answer = 0

    for i in range(len(board)):  # board 배열로 만들기
        popped = board.pop(0)
        board.append([p for p in popped])

    while True:  # 터진 블록이 없을 때까지 반복
        checked = []  # 이번 턴에 터져야 할 블록들 모음
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == "0":  # 이미 블록이 터져 빈 자리면 패스
                    continue
                if board[i][j] == board[i][j + 1]:  # 연속으로 두 개가 동일한 블록이면, 밑에 두 개도 동일한지 확인
                    if board[i][j] == board[i + 1][j] and board[i][j + 1] == board[i + 1][j + 1]:
                        checked.append((i, j))
                        checked.append((i, j + 1))
                        checked.append((i + 1, j))
                        checked.append((i + 1, j + 1))  # 터져야 할 블록들 전부 저장

        if len(checked) == 0:  # 이번에 터진 블록이 없으면 종료
            break
        else:
            answer += len(set(checked))  # 모아둔 블록 다 터뜨리기!
            for c in checked:
                board[c[0]][c[1]] = '0'

            for c in reversed(checked):  # 블록들 내리기
                check_n = c[0] - 1
                put_n = c[0]

                while check_n >= 0:  # 터진 자리 위에 있는 블록들을 다 내린다.
                    if board[put_n][c[1]] == "0" and board[check_n][c[1]] != "0":
                        board[put_n][c[1]] = board[check_n][c[1]]
                        board[check_n][c[1]] = "0"
                        put_n -= 1

                    check_n -= 1

    return answer

# def solution(판의_높이, 폭, 판의_배치_정보):
#     print('-----------------------------')
#     answer = 0
#
#     for _ in range(len(판의_배치_정보)):
#         보드_열 = 판의_배치_정보.pop(0)
#         print('보드_열 = {}'.format(보드_열))
#         판의_배치_정보.append([보드_열_값 for 보드_열_값 in 보드_열])
#
#     터진_블록이_없을_때까지_반복 = True
#     while 터진_블록이_없을_때까지_반복:
#         이번_턴에_터져야_하는_블록_모음 = []
#         for 높이_인덱스 in range(판의_높이 - 1):
#             for 폭_인덱스 in range(폭 - 1):
#                 이미_블록이_터져_빈_자리 = "0"
#                 if 판의_배치_정보[높이_인덱스][폭_인덱스] == 이미_블록이_터져_빈_자리:
#                     continue
#
#                 연속으로_두_개가_동일한_블록 = 판의_배치_정보[높이_인덱스][폭_인덱스] == 판의_배치_정보[높이_인덱스][폭_인덱스 + 1]
#                 if 연속으로_두_개가_동일한_블록:
#                     바로_아래_블록 = 판의_배치_정보[높이_인덱스][폭_인덱스] == 판의_배치_정보[높이_인덱스 + 1][폭_인덱스]
#                     바로_아래_오른쪽_블록 = 판의_배치_정보[높이_인덱스][폭_인덱스 + 1] == 판의_배치_정보[높이_인덱스 + 1][폭_인덱스 + 1]
#                     if  바로_아래_블록 and 바로_아래_오른쪽_블록:
#                         # 터져야 하는 블록 저장
#                         이번_턴에_터져야_하는_블록_모음.append((높이_인덱스, 폭_인덱스))
#                         이번_턴에_터져야_하는_블록_모음.append((높이_인덱스, 폭_인덱스 + 1))
#                         이번_턴에_터져야_하는_블록_모음.append((높이_인덱스 + 1, 폭_인덱스))
#                         이번_턴에_터져야_하는_블록_모음.append((높이_인덱스 + 1, 폭_인덱스 + 1))
#
#         print('이번_턴에_터져야_하는_블록_모음 = {}'.format(이번_턴에_터져야_하는_블록_모음))
#         이번에_터진_블록이_없다 = 0
#         if len(이번_턴에_터져야_하는_블록_모음) == 이번에_터진_블록이_없다:
#             break
#         else:
#             answer += len(set(이번_턴에_터져야_하는_블록_모음))
#             for 블록_정보 in 이번_턴에_터져야_하는_블록_모음:
#                 높이 = 블록_정보[0]
#                 폭 = 블록_정보[1]
#                 판의_배치_정보[높이][폭] = '0'
#
#             for 블록_정보 in reversed(이번_턴에_터져야_하는_블록_모음):  # 블록들 내리기
#                 높이 = 블록_정보[0]
#                 폭 = 블록_정보[1]
#                 터진_자리_위에_있는_블록 = 높이 - 1
#
#                 while 터진_자리_위에_있는_블록 >= 0:  # 터진 자리 위에 있는 블록들을 다 내린다.
#                     if 판의_배치_정보[높이][폭] == "0" and 판의_배치_정보[터진_자리_위에_있는_블록][폭] != "0":
#                         판의_배치_정보[높이][폭] = 판의_배치_정보[터진_자리_위에_있는_블록][폭]
#                         판의_배치_정보[터진_자리_위에_있는_블록][폭] = "0"
#                         높이 -= 1
#
#                     터진_자리_위에_있는_블록 -= 1
#
#     return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))