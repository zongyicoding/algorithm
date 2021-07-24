
def fib(i):
    if i == 0:
        return 0
    elif i ==1 or i==2:
        return 1
    else:
        return fib(i-1) + fib(i-2)

if __name__=='__main__':
    number = int(input('請輸入第幾個費式數列:'))
    for idx in range(0, number):
        ans = fib(idx)
        print(f'fib{idx+1}: {ans}')