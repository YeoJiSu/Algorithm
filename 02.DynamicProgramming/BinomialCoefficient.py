# n-1 C k-1 + n-1 C k   = n C k 였다 !! 
def recursive(n,k):
    if k==0 or k==n:
        return 1
    else:
        return recursive(n-1,k-1)+recursive(n-1,k)
def dynamicProgramming(n,k):
    """
      k)  0 1 2 3 4
         ___________
    n=0 | 1
    n=1 | 1 1
    n=2 | 1 2 1
    n=3 | 1 3 3 1
    n=4 | 1 4 6 4 1
    """
    # 참고: Python에서는 * 연산자를 이용해 배열을 선언하게 되면, 얕은 복사(shallow copy)가 진행된다.
    coef = [[0 for i in range(k+1)] for i in range(n+1)] 
    
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                coef[i][j] = 1
            else:
                coef[i][j] = coef[i-1][j-1]+coef[i-1][j]
    return coef[n][k]

print(recursive(5,3))
print(dynamicProgramming(5,3))
