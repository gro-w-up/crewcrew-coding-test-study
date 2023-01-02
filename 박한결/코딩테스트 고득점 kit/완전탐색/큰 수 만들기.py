
'''
풀이 및 접근방법

 1. 일단 number의 첫번째 값을 스택에 세팅한다.
 2. number의 각 자리마다 stack에 추가하면서, stack의 마지막값과 number의 추가되는 값(이전값과 다음값)을 비교한다.
 3. 이전값이 다음값보다 적으면 stack에서 비운다.
 4. stack에 남은 값들을 합쳐서 리턴한다.
'''

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)