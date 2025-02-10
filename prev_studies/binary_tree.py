class TreeNode: # 노드를 생성하는 클래스
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root: # 뿌리 노드가 비어 있으면
            self.root = TreeNode(value) # 뿌리 노드에 노드 생성하여 값 할당
        else:
            self._insert_recursive(self.root, value) # 비어 있지 않으면 맞는 위치에 value를 가지는 노드를 추가하도록 부모노드를 기준으로 하는 _insert_recursive 호출

    def _insert_recursive(self, node, value): # 부모 노드의 값과 value를 비교한 뒤 가야할 방향에 따라(작으면 왼쪽, 크면 오른쪽) 왼쪽 자식 노드와 오른쪽 자식 노드가 비어있는 확인 하고 비어있으면 추가, 안비어있으면 재귀호출을 통해 계속 내려간다. 
        if value < node.val: # 부모 노드의 값이 value보다 크면
            if node.left: # 왼쪽 자식 노드가 안 비어 있으면
                self._insert_recursive(node.left, value) # 왼쪽 자식 노드를 부모 노드로 해서 위의 _insert_recursive의 매커니즘을 반복하여 알맞은 위치에 value를 값으로 가지는 노드 생성
            else: # 비어있으면 left에 value를 값으로 가지는 노드 생성 
                node.left = TreeNode(value)
        elif value > node.val: # 부모 노드의 값이 value보다 작으면 
            if node.right: # 오른쪽 자식 노드가 안비어있으면
                self._insert_recursive(node.right, value) # 오른쪽 자식 노드를 부모 노드로 해서...
            else: # 비어있으면 right에 value를 값으로 가지는 노드 생성
                node.right = TreeNode(value)

    def search(self, value): # 검색 메소드
        return self._search_recursive(self.root, value) # 뿌리 노드를 시작으로 하는 재귀 검색 메소드를 시작으로 호출한다.

    def _search_recursive(self, node, value): # 부모 노드를 기준으로 value값을 부모 노드가 비어있으면 존재하지 않는 거로 반환, 부모 노드의 값이 value면 True 반환 부모 노드의 값이 value 보다 크면 왼쪽 자식 노드를 부모 노드로하여 재귀 검색 메서드 재귀호출, 작으면 오른쪽 자식 노드를 부모 노드로 하여 재귀 검색 메서드 재귀호출 하여 찾는다. 있으면 True 없으면 False
        if not node:
            return False
        if node.val == value:
            return True
        if value < node.val:
            return self._search_recursive(node.left, value)
        if value > node.val:
            return self._search_recursive(node.right, value)
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return None

        if value < node.val:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.val:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: 리프 노드인 경우
            if not node.left and not node.right:
                return None

            # Case 2: 하나의 자식 노드를 가진 경우
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: 두 개의 자식 노드를 가진 경우
            successor = self._find_min(node.right)
            node.val = successor.val
            node.right = self._delete_recursive(node.right, successor.val)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
코드 설명:

1. `TreeNode` 클래스는 트리의 각 노드를 나타냅니다. 노드는 값(val)과 왼쪽 자식 노드(left), 오른쪽 자식 노드(right)를 가집니다.
2. `BinaryTree` 클래스는 이진 트리 자료구조를 나타냅니다. 루트 노드(root)를 가지며, 삽입(insert)과 검색(search) 연산을 지원합니다.
3. `insert` 메소드는 트리에 새로운 값을 삽입합니다. 트리가 비어있다면 루트 노드를 생성하고, 그렇지 않다면 `_insert_recursive` 메소드를 호출하여 재귀적으로 삽입 위치를 찾아 새 노드를 삽입합니다.
4. `_insert_recursive` 메소드는 재귀적으로 삽입 위치를 찾아 새 노드를 삽입합니다. 삽입하려는 값이 현재 노드의 값보다 작으면 왼쪽 서브트리에 삽입하고, 크면 오른쪽 서브트리에 삽입합니다. 삽입 위치에 노드가 없다면 새 노드를 생성합니다.
5. `search` 메소드는 특정 값을 트리에서 검색합니다. `_search_recursive` 메소드를 호출하여 재귀적으로 검색을 수행합니다.
6. `_search_recursive` 메소드는 재귀적으로 트리를 탐색하며 값을 검색합니다. 현재 노드가 검색하려는 값과 같으면 True를 반환하고, 검색 값이 현재 노드의 값보다 작으면 왼쪽 서브트리에서 검색을, 크면 오른쪽 서브트리에서 검색을 진행합니다. 검색 값이 트리에 없다면 False를 반환합니다.

트리 자료구조는 데이터의 계층적 구조를 표현하는 데 유용하며, 효율적인 검색, 삽입, 삭제 연산을 제공합니다. 위의 코드는 이진 탐색 트리(Binary Search Tree)의 기본적인 구현으로, 왼쪽 서브트리의 모든 노드의 값은 현재 노드의 값보다 작고, 오른쪽 서브트리의 모든 노드의 값은 현재 노드의 값보다 큰 특성을 유지합니다.

삭제 연산을 수행하는 `delete` 메서드와 재귀적으로 삭제를 수행하는 `_delete_recursive` 메서드를 추가했습니다. `_delete_recursive` 메서드는 다음 세 가지 경우를 처리합니다:

1. 삭제하려는 노드가 리프 노드인 경우: 해당 노드를 None으로 만들어 삭제합니다.
2. 삭제하려는 노드가 하나의 자식 노드를 가진 경우: 해당 노드를 자식 노드로 대체합니다.
3. 삭제하려는 노드가 두 개의 자식 노드를 가진 경우: 오른쪽 서브트리에서 가장 작은 값을 가진 노드(successor)를 찾아 삭제하려는 노드의 값을 대체하고, successor를 삭제합니다.

point : 이진 트리는 삽입, 검색, 삭제, 노드 생성의 기능이 있으며, 노드가 없으면 생성을 통한 값 할당, 있으면 비교를 통한 값 할당. 

      찾을 때도 뿌리 노드 부터 시작해서 노드에 값이 존재하는 지 부터 확인 그 후 비교를 통한 재귀호출.
