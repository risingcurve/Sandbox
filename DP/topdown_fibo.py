memo = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if memo[x] != 0:
        return memo[x]

    memo[x] = fibo(x-1) + fibo(x-2)
    return memo[x]

print(fibo(int(input())))