# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?h_r=profile

def euler(N: int) -> int:
    N -= 1
    _sum = 0
    
    m = N//3
    _sum = 3*(m*(m+1))//2

    m = N//5
    _sum += 5*(m*(m+1))//2

    m = N//15
    _sum -= 15*(m*(m+1))//2

    return _sum


if __name__ == "__main__":
    # N = 10
    N = 100
    print(euler(N))

