'''
count n!
sample:
4! = 4*3*2*1
'''

def get_ans(n):
    ans = 1
    for idx in range(n, 0,-1):
        ans = ans * idx
    return ans

if __name__=='__main__':
    n = int(input('input: '))
    ans = get_ans(n)
    print(ans)
