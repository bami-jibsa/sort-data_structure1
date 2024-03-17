#이진 트리

class Node: #노드 생성하는거
	def __init__(self, item):
		self.item = item
		self.left = None
		self.right = None
		
#노드 만들기
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

class Binary_Tree(): #노드를 엮어서 트리로 만들기
	def __init__(self):
		self.root = None

#노드 트리에 넣기	
tree = Binary_Tree()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

class order():
	def preorder(self, n): # 자기 자신 출력 -> 왼쪽 서브 트리 호출 -> 오른쪽 서브 트리 호출
		if n!= None:
			print(n.item, '', end='') # 트리에서 노드 가져오기
			if n.left:
				self.preorder(n.left)  # 왼쪽 서브 트리 순회
			if n.right:
				self.preorder(n.right)  # 오른쪽 서브 트리 순회
				
	def postorder(self, n): # 왼쪽 서브 트리 호출 -> 오른쪽 서브 트리 호출 -> 자기 자신 출력
		if n!= None:
			if n.left:
				self.postorder(n.left)
			if n.right:
				self.postorder(n.right)
			print(n.item, '', end=' ')
			
	def inorder(self, n): # 왼쪽 서브 트리 호출 -> 자기 자신 출력 -> 오른쪽 서브 트리 호출
		if n!= None:
			if n.left:
				self.postorder(n.left)
			print(n.item, '', end=' ')
			if n.right:
				self.postorder(n.right)
				
a = order()
a = a.preorder(n1)
