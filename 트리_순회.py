
import sys
input = sys.stdin.readline

# 1. 노드 클래스 정의 먼저!
class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

# 2. 입력 처리
n = int(input())
inputs = [input().split() for _ in range(n)]

# 3. 트리 구성
tree = {}
for item, left, right in inputs:
    tree[item] = Node(item, left, right)

# 4. 전위 순회: 루트 → 왼쪽 → 오른쪽
def preorder(node):
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

# 5. 중위 순회: 왼쪽 → 루트 → 오른쪽
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])

# 6. 후위 순회: 왼쪽 → 오른쪽 → 루트
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')

# 7. 순회 실행
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

