from itertools import combinations
'''
타임오버~
def solution(number, k):
    answer = list(combinations(list(number), len(number)-k))
    print(answer)
    sortedArray =sorted(answer,reverse=True)[0]
    print(sortedArray)
    return ''.join(sortedArray)
'''
def solution(number, k):
    st = []
    for i in range(len(number)):
        #스택이 비지 않고, K만큼 아직 제거가 안되었으며, 스택에 이전 값보다 지금 값이 큰경우
        while st and k > 0 and st[-1] < number[i]:
            #한마디로 지금 내 숫자보다 작으면 팝
            st.pop()
            # 하나 지워주기
            k -= 1
            #큰수 스택에 append
        st.append(number[i])
    print(st[:len(st)-k]) # 이것의 의미는 4번 케이스 처럼 5,4,3,2,1, 1개를 버리기 위해서
    return ''.join(st[:len(st) - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("54321", 1))