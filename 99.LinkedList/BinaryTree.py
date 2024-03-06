class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# pre-order Traversal        
def pre_order(node):
    # root -> 왼 -> 오
    print(node.val, end=' ')
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

# in-order Traversal        
def in_order(node):
    # 왼 -> root -> 오
    if node.left:
        in_order(node.left)
    print(node.val, end=' ')
    if node.right:
        in_order(node.right)

# post-order Traversal        
def post_order(node):
    # 왼 -> 오 -> root
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.val, end=' ')

N1 = Node('A')
N2 = Node('B')
N3 = Node('C')
N4 = Node('D')
N5 = Node('E')
N6 = Node('F')
N7 = Node('G')


N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7

print('preorder')
pre_order(N1)

print('\ninorder')
in_order(N1)

print('\npostorder')
post_order(N1)
