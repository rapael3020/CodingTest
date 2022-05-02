import math

def get_prime(b):                   # b=30
    e = int(math.sqrt(b)) + 1       # e=5
    is_prime = [0] * e              # is_prime[x] = 0 -> prime number, 1->prime number아님
    prime = []
    for i in range (2, e):
        if is_prime[i] == 0:
            prime.append(i)         # i는 prime 목록에 추가
            for x in range(i+i, e, i):
                is_prime[x] = 1
            return prime
        
def answer(a,b):
    prime = get_prime(b)
    for p in prime:
        t1, t2 = p**2, p**3
        if a<=t1<=b: answer
    answer = 0
    return answer