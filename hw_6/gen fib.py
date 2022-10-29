def gen_fib(n):
    if n ==1:
        print (0)
        return 
    fib1 = 0
    fib2 = 1

    for i in range(n):
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
 
for fib in gen_fib(4):
    print(fib, end=' ')

