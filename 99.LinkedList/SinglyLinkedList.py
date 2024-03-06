class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 노드 추가 
# 값이 0인 첫번재 노드 
head = ListNode(0) 

# 값이 1인 두번째 노드 
head.next = ListNode(1)
curr_node= head.next

curr_node.next = ListNode(2)
curr_node=curr_node.next

curr_node.next = ListNode(3)
curr_node=curr_node.next

curr_node.next = ListNode(4)
curr_node=curr_node.next

# 전체 연결리스트 출력 (탐색)
node=head
while node:
    print(node.val)
    node=node.next

# 노드 탐색하여 삭제 
#delete node by value
node=head
while node.next:
    if node.next.val==2:
        next_node=node.next.next
        node.next=next_node
        break
    node=node.next
    
node=head
while node:
    print(node.val)
    node=node.next
''' 출력결과 : 0,1,3,4 '''
