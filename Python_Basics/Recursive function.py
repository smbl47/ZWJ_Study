def put(n):
    if n == 1:
        return 1
    else:
        res = n * put(n - 1)
        return res


print(put(6))


# 斐波那契函数
def Fibonacci_function(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        result = Fibonacci_function(n - 1) + Fibonacci_function(n - 2)
        return result


print(Fibonacci_function(8))

for i in range(1,9):
    print(Fibonacci_function(i))
