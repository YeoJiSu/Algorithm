num = 10

"""
재귀 함수
시간복잡도: O(2^n) => 재귀 함수의 시간 복잡도는 지수 시간복잡도. 각각의 호출이 두 번의 호출을 만들기 때문.
공간복잡도: O(n) => 호출 스택의 크기에 비례
"""
def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive(n-1)+recursive(n-2)
# 0 1 1 2 3 5 8 ... 
print(recursive(num))

"""
동적계획법 함수
시간복잡도: O(n)
공간복잡도: O(n)
"""
def dynamic(n):
    _list = [0]*(n+1)
    _list[1] = 1
    for i in range(2, n+1):
        _list[i] = _list[i-1]+_list[i-2]
    return _list[n]

print(dynamic(num))
