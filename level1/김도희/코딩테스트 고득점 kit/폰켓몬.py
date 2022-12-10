'''
풀이 및 접근방법


'''

def solution(nums):
    answer = 0

    choosed = len(nums) // 2
    nums = set(nums)

    return min(choosed, len(nums))