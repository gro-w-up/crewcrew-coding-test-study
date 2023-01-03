'''
풀이 및 접근방법

 1. 제공되는 좌표계가 거꾸로되어있으므로, puddles도 거꾸로 뒤집어준다.
 2. dp에 주어진 n,m만큼의 공간을 리스트로 세팅한다.
 3. dp에서 1,1좌표를 초기값으로 1 세팅한다.
 4. x축을 i, y축을 j로 해서 이중반복한다.
 5. 만약 dp에서 i,j 좌표가 puddles에 있으면 0을 넣는다.
 6. 아니라면 왼쪽, 오른쪽 값의 합의 1000000007로 나눈 값을 넣는다.
 7. dp의 n,m좌표의 값을 리턴한다.
'''

def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:
                dp[i][j] = 0
            else:  
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]