# Dynamic Programming

# Recursive Backtracking
def f(n):
    """Time complexity is really O(2^n)"""
    if n == 0:
        return 0
    if n == 1:
        return 1

    return f(n - 1) + f(n - 2)


# Memoization
# first cut
def f_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = f_memo(n - 1, memo) + f_memo(n - 2, memo)
    return memo[n]


# Top-Down DP(Momoization)


def fib(n):
    """Really this time complexity is O(n)"""
    memo = {0: 0, 1: 1}

    def f(n):
        if n in memo:
            return [n]

        memo[n] = f(n - 1) + f(n - 2)
        return memo[n]

    return f(n)


# Bottom-Up DP (tabulation)
def fib_but(n):
    """TComplexity is O(n)"""
    dp = [0, 1]
    for i in range(2, n + 1):
        new = dp[i - 2] + dp[i - 1]
        dp.append(new)
    return dp[n]


# Bottom-Up No-Memory DP
def fib_bup(n):
    if n < 2:
        return n

    prev, cur = 0, 1
    for i in range(2, n + 1):
        prev, cur = cur, cur + prev

    return cur
