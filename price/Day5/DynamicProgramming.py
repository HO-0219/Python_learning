#동적 계획법


# 피보나치 수열 예제 (일반 재귀 vs DP)
# 일반 재귀 피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

# 동적계획법(DP)를 이용한 메모이제이션 (top-down, 재귀+캐싱)

def fibonacci_memo(n,memo={}):
    if n in memo:
        return memo[n]
    if n <=1:
        return n
    memo[n] = fibonacci_memo(n-1,memo) + fibonacci_memo(n-2,memo)
    return memo[n]
#1,1,2,3,5,8,13,21,34,55
#1 ,1 , (1+1), (1+(1+1)), (1+1) + (1+(1+1), (1+(1+1))+(1+1) + (1+(1+1) )

print(fibonacci_memo(4))

# 동적 계획법 DP 중 타뷸레이션 bottom-up , 반복
def fibonacci_tab(n):
    dp = [0] * (n + 1)
    dp[1] = 1  # 초기값 설정

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(fibonacci_tab(5))  # 55
