def solution(n, lost, reserve):

    print('-------------------')

    # 제한사항
    if n > 30 and n < 2 :
        return 0

    # 전체 학생 수는 2명 이상
    # 도난당한 학생은 1명 이상
    # 여벌 체육복을 가져온 학생은 1명 이상
    # 따라서, 항상 수업을 들을 수 있는 학생의 수는 1명이다.
    answer = 1

    # 모든 학생들이 체육복을 1개씩 가지고 왔다고 가정
    students = [1] * (n)
    print('초기 학생들 체육복 배열 :', students)

    # 도난당한 학생의 체육복 파악 - 1
    for lost_student_no in lost:
        students[lost_student_no - 1] -= 1
    print('도난당한 학생의 체육복 : ', students)

    # 여분이 있는 학생의 체육복 개수 + 1
    for reverse_student_no in reserve:
        students[reverse_student_no - 1] += 1
    print('여분이 있는 학생의 체육복 : ', students)


    #  빌려주는 처리
    for student_no in range(1, n):

        # 앞번호 처리
        if students[student_no] == 2 and student_no > 0 and students[student_no - 1] == 0:
            students[student_no] -= 1
            students[student_no -1] += 1;

        # 뒷번호 처리
        if students[student_no] == 2 and student_no < n and students[student_no + 1] == 0:
            students[student_no] -= 1
            students[student_no -1] += 1;

    print('빌려준 후 학생들의 체육복 상태 : ', students)

    for student_no in range(1, n):
        if students[student_no] > 0:
            answer += 1

    return answer

# expect 5
print(solution(5, [2, 4], [1, 3, 5] ))
# expect 4
print(solution(5, [2, 4], [3] ))
# expect 2
print(solution(3, [3], [1] ))


"""
문제풀이 및 접근방법
    - 참고자료
        https://velog.io/@kyunghwan1207/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98Greedy-Algorithm-%ED%83%90%EC%9A%95%EB%B2%95
    - 문제 단순화
        일부 학생이 체육복 도난, 여벌 체육복이 있는 학생이 빌려준다.
        학생들 번호는 체격 순이고 바로 앞번호 학생이나 바로 뒷번호의 학생에게만 빌려줄 수 있다.
        1 2 3 <- 4 -> 5
        1 <- 2 -> 3 4 5
        체육복이 없으면 수업 들을 수 없으니 적절히 빌려 최대한 많은 학생이 체육 수업을 들어야함
"""

"""
실행 결과
    테스트 1
    입력값 〉	5, [2, 4], [1, 3, 5]
    기댓값 〉	5
    실행 결과 〉	테스트를 통과하였습니다.
    테스트 2
    입력값 〉	5, [2, 4], [3]
    기댓값 〉	4
    실행 결과 〉	테스트를 통과하였습니다.
    테스트 3
    입력값 〉	3, [3], [1]
    기댓값 〉	2
    실행 결과 〉	테스트를 통과하였습니다.
    
정확성  테스트
    테스트 1 〉	실패 (0.01ms, 10.2MB)
    테스트 2 〉	실패 (0.01ms, 10.3MB)
    테스트 3 〉	통과 (0.01ms, 10.2MB)
    테스트 4 〉	실패 (0.01ms, 10.2MB)
    테스트 5 〉	통과 (0.01ms, 10.3MB)
    테스트 6 〉	통과 (0.01ms, 10.3MB)
    테스트 7 〉	실패 (런타임 에러)
    테스트 8 〉	실패 (0.01ms, 10.2MB)
    테스트 9 〉	실패 (0.01ms, 10.4MB)
    테스트 10 〉	통과 (0.02ms, 10.2MB)
    테스트 11 〉	통과 (0.01ms, 10.2MB)
    테스트 12 〉	실패 (런타임 에러)
    테스트 13 〉	통과 (0.01ms, 10.2MB)
    테스트 14 〉	통과 (0.01ms, 10.3MB)
    테스트 15 〉	통과 (0.01ms, 10.1MB)
    테스트 16 〉	통과 (0.01ms, 10.2MB)
    테스트 17 〉	실패 (0.01ms, 10.4MB)
    테스트 18 〉	실패 (0.01ms, 10.3MB)
    테스트 19 〉	실패 (0.01ms, 10.2MB)
    테스트 20 〉	실패 (0.01ms, 10.3MB)
    테스트 21 〉	실패 (0.01ms, 10.4MB)
    테스트 22 〉	통과 (0.00ms, 10.2MB)
    테스트 23 〉	실패 (0.01ms, 10.1MB)
    테스트 24 〉	통과 (0.01ms, 10.2MB)
    테스트 25 〉	실패 (0.01ms, 10.4MB)
채점 결과
    정확성: 44.0
    합계: 44.0 / 100.0
"""

"""
다른사람의 풀이
def solution(n, lost, reserve):
    set_r = set(reserve) - set(lost)
    set_l = set(lost) - set(reserve)

    for r in set_r:
        if r-1 in set_l:
            set_l.remove(r-1)
        elif r+1 in set_l:
            set_l.remove(r+1)

    return n - len(set_l)
"""