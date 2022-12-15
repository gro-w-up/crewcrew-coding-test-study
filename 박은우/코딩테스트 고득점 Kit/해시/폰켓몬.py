def solution(nums):
    return min(len(nums) // 2, len(set(nums)))

# 테스트 케이스
print('result 1 : ', solution([3,1,2,3]))
print('result 2 : ', solution([3,3,3,2,2,4]))
print('result 3 : ', solution([3,3,3,2,2,2]))