from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_set = Counter([str1[i:i+2] for i in range(len(str1) - 1) if str1[i:i+2].isalpha()])
    str2_set = Counter([str2[i:i + 2] for i in range(len(str2) - 1) if str2[i:i+2].isalpha()])

    intersect_key = set(str1_set.keys()) & set(str2_set.keys())
    union_key = set(str1_set.keys()) | set(str2_set.keys())

    sum_intersect = sum([min(str1_set[key], str2_set[key]) for key in intersect_key])
    sum_union = sum([max(str1_set[key], str2_set[key]) for key in union_key])

    #집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1
    if not intersect_key and not union_key:
        return 65536
    #겹치는 글자가 없으므로 유사도 0
    elif not intersect_key and union_key:
        return 0
    else:
        return int(sum_intersect / sum_union * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))