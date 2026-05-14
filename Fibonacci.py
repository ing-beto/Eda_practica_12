dp=[1, 1]

def fib_asc(n):
    if n == 0 or n ==1:
        return dp[n]
    
    while len(dp) <= n:
        dp.apend(dp[-1]+ dp[-2])
    return dp[n]

def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)
memoria = {}
def fib_des(n):
    if n in memoria:
        return memoria[n]
    if n == 0 or n == 1:
        return 1
    memoria[n] = fib_des(n-1) + fib_des(n-2)
    return memoria[n]
