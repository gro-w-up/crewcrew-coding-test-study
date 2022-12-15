def solution(nums):
    max = len(nums) // 2

    count = set()
    for i in nums:
        count.add(i)

    if max >= len(count):
        return len(count)
    else:
        return max


print('result 1 : ', solution([3, 1, 2, 3]))
