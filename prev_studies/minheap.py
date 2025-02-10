최소 힙이란 완전 이진 트리의 일종으로, 부모 노드의 값이 항상 자식 노드의 값보다 작거나 같은 성질을 만족하는 자료구조입니다. 최소 힙에서는 루트 노드에 가장 작은 값이 위치하게 됩니다.

파이썬에서는 heapq 라이브러리를 통해 최소 힙을 쉽게 구현할 수 있지만, 여기서는 heapq를 사용하지 않고 직접 최소 힙을 구현해보겠습니다.

최소 힙을 포함한 이진 힙에서 자식 노드와 부모 노드의 인덱스 사이에는 다음과 같은 관계가 성립합니다.

1. 왼쪽 자식 노드의 인덱스 = (부모 노드의 인덱스) * 2 + 1
2. 오른쪽 자식 노드의 인덱스 = (부모 노드의 인덱스) * 2 + 2
3. 부모 노드의 인덱스 = (자식 노드의 인덱스 - 1) // 2

이러한 관계는 이진 힙을 배열로 표현할 때 나타나는 특징입니다. 배열의 인덱스가 0부터 시작한다고 가정하면, 위와 같은 공식이 성립합니다.

예를 들어, 어떤 노드의 인덱스가 4라면:

- 왼쪽 자식 노드의 인덱스 = 4 * 2 + 1 = 9
- 오른쪽 자식 노드의 인덱스 = 4 * 2 + 2 = 10
- 부모 노드의 인덱스 = (4 - 1) // 2 = 1

이를 그림으로 나타내면 다음과 같습니다.

        1
      /   \
     2     3
   /  \   /  \
  4    5 6    7


위 예시에서 인덱스 4인 노드의 왼쪽 자식은 인덱스 9, 오른쪽 자식은 인덱스 10이며, 부모는 인덱스 1입니다.

이러한 인덱스 관계를 이용하면 이진 힙에서 특정 노드의 부모 노드나 자식 노드를 쉽게 찾을 수 있습니다. 이는 힙의 핵심 연산인 삽입(sift up)과 삭제(sift down)에서 중요한 역할을 합니다.

- 삽입 시에는 새 노드를 배열의 마지막에 추가한 후, 부모 노드와 비교하며 위로 올라갑니다.
- 삭제 시에는 루트 노드를 제거하고 마지막 노드를 루트로 옮긴 후, 자식 노드와 비교하며 아래로 내려갑니다.

이 과정에서 부모와 자식 노드의 인덱스를 쉽게 계산할 수 있어야 효율적인 연산이 가능합니다.

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val) # 리스트의 마지막에 노드를 새로 추가한 뒤
        self._sift_up(len(self.heap) - 1) # 현 리스트의 마지막 인덱스를 idx로 해서 _sift_up 호출하여 추가한 val이 맞는 위치를 찾아가도록 한다.

    def pop(self):
        if not self.heap: # 리스트가 비어있다면
            return None # 아무것도 반환하지 않는다.
        if len(self.heap) == 1: # 리스트에 하나만 존재한다면
            return self.heap.pop() # pop을 이용해 반환
        min_val = self.heap[0] # 리스트에 두개 이상의 값이 존재하면 최소값은 뿌리노드이므로 min_val에 최소값을 할당하고
        self.heap[0] = self.heap.pop() # 마지막 인덱스의 값을 뿌리 노드로 이동
        self._sift_down(0) # idx = 0 으로 _sift_down 호출
        return min_val

    def _sift_up(self, idx):
        parent = (idx - 1) // 2 # idx : 자식 노드의 인덱스
        while idx > 0 and self.heap[parent] > self.heap[idx]: # 자식 노드가 있고, 부모 노드가 자식 노드보다 큰 동안(정렬된 상태는 부모노드가 항상 자식 노드보다 작거나 같아야 하므로)
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent] # 자식 노드와 부모 노드를 스왑
            idx = parent # 기존의 자식 노드의 인덱스였던 idx를 기존의 부모 노드의 인덱스로 바꾸고
            parent = (idx - 1) // 2 # 바뀐 자식 노드의 인덱스의 부모 노드를 인덱스를 parent에 할당하여 계속 위로 올라가며 비교한다.

    def _sift_down(self, idx): 
        left = 2 * idx + 1 # idx의 왼쪽 자식 노드 인덱스
        right = 2 * idx + 2 # idx의 오른쪽 자식 노드 인덱스
        smallest = idx 
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]: # 리스트의 길이가 왼쪽 자식 노드의 인덱스보다 크고 왼쪽 자식 노드의 값이 부모 노드의 값보다 작으면 smallest는 왼쪽 자식 노드의 인덱스가 된다. 
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]: # 이경우는 오른쪽 자식노드가 부모 노드보다 작은 경우로 smallest는 오른쪽 자식 노드의 인덱스가 된다. 위에서 부터 차례대로 내려오므로 왼쪽 자식 노드부터 비교하며 내려온다.
            smallest = right
        if smallest != idx: # 위의 두 조건문의 결과로 처음 부모 노드의 인덱스 idx와 smallest의 값이 다르게 되어버리면(자식 노드의 값이 부모 노드보다 작은 경우가 있을 때) 부모 노드보다 작은 자식 노드와 부모 노드의 값 스왑 
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest) # 스왑되기 전의 부모 노드보다 작은 자식 노드의 인덱스를 부모 인덱스로 하여 _sift_down을 재귀호출하여 밑으로 내려가며 비교해여 스왑을 이용해 정렬한다.


'''
이제 위 코드의 동작 방식을 단계별로 살펴보겠습니다. 예시로 3, 9, 2, 8 네 개의 값을 차례로 최소 힙에 삽입(push)하는 과정을 보겠습니다.

1. MinHeap.push(3)
    - self.heap = [3]
    - _sift_up(0) 호출 (idx = 0)
        - idx가 0이므로 반복문 진입하지 않음
    - 결과: self.heap = [3]
2. MinHeap.push(9)
    - self.heap = [3, 9]
    - _sift_up(1) 호출 (idx = 1)
        - parent = 0, self.heap[0] = 3 < 9 이므로 반복문 진입하지 않음
    - 결과: self.heap = [3, 9]
3. MinHeap.push(2)
    - self.heap = [3, 9, 2]
    - _sift_up(2) 호출 (idx = 2)
        - parent = 0, self.heap[0] = 3 > 2 이므로 swap 발생
        - self.heap = [2, 9, 3], idx = 0
    - 결과: self.heap = [2, 9, 3]
4. MinHeap.push(8)
    - self.heap = [2, 9, 3, 8]
    - _sift_up(3) 호출 (idx = 3)
        - parent = 1, self.heap[1] = 9 > 8 이므로 swap 발생
        - self.heap = [2, 8, 3, 9], idx = 1
        - parent = 0, self.heap[0] = 2 < 8 이므로 반복문 종료
    - 결과: self.heap = [2, 8, 3, 9]

이제 최소 힙에서 가장 작은 값을 꺼내는(pop) 과정을 보겠습니다.

1. MinHeap.pop()
    - min_val = self.heap[0] = 2
    - self.heap[0] = 9 (마지막 값을 루트로 이동)
    - self.heap = [9, 8, 3]
    - _sift_down(0) 호출 (idx = 0)
        - left = 1, right = 2
        - self.heap[1] = 8 < 9 이므로 smallest = 1
        - self.heap[2] = 3 < 8 이므로 smallest = 2
        - idx != smallest 이므로 swap 발생
        - self.heap = [3, 8, 9], idx = 2
        - left = 5, right = 6 (범위 벗어남)
    - 결과: self.heap = [3, 8, 9], 반환값 = 2

위와 같은 과정을 통해 최소 힙이 구현됩니다. 새로운 값을 삽입할 때는 맨 뒤에 추가한 후 부모 노드와 비교하며 위로 올라가고(sift up), 가장 작은 값을 꺼낼 때는 마지막 노드를 루트로 옮긴 후 자식 노드와 비교하며 아래로 내려가는(sift down) 방식입니다.

이를 통해 항상 루트 노드에 최소값이 위치하게 되며, 값의 삽입과 삭제가 O(log n)의 시간 복잡도로 이루어집니다.
'''
