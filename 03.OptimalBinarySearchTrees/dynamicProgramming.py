inf = float("inf")
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def optimalSearchTree(n, p):
    A = [[0 for x in range(0, n+1)] for y in range(0,n+1)]
    R = [[0 for x in range(0, n+1)] for y in range(0,n+1)]
    
    for i in range(0,n):
        A[i][i+1] = p[i]
        R[i][i+1] = i+1
    
    last = n-1
    term = 2
    for col in range(0, n-1): # n-2 만큼 
        for i in range(0, last):
            j = i+term
            mini = inf
            mini_key = None
            for key in range(i+1, j+1):
                if A[i][key-1] + A[key][j] < mini:
                    mini = A[i][key-1] + A[key][j]
                    mini_key = key
            A[i][j] = mini + sum(p[i:j])
            R[i][j] = mini_key
        term += 1
        last -= 1
    
    print(A)
    print(R)
    return A, R


n = 4
p = [4,2,6,3]
A, R = optimalSearchTree(n, p)

def optimalBST_build(i, j, R, Keys):
    k = R[i][j]
    if k == 0:
        return
    else:
        print(k)
        node = TreeNode(Keys[k-1])
        node.left = optimalBST_build(i, k-1, R, Keys)
        node.right = optimalBST_build(k, j, R, Keys)
        return node

optimalBST_build(0,4,R,p)