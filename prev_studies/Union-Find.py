1. 유니온 파인드(Union-Find)는 서로소 집합(Disjoint Set)을 관리하는 자료구조입니다. 서로소 집합이란 교집합이 없는 집합들을 말합니다. 유니온 파인드는 여러 개의 집합을 관리하고, 두 집합을 합치는 연산(Union)과 어떤 원소가 어느 집합에 속하는지 찾는 연산(Find)을 제공합니다.
   유니온 파인드는 일반적으로 배열이나 트리 구조를 사용하여 구현됩니다. 배열을 사용하는 경우, 각 원소는 자신이 속한 집합의 대표 원소(부모)를 가리키게 됩니다. 초기에는 모든 원소가 자기 자신을 가리키는 상태로 시작합니다.

  class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) # 처음은 자신의 부모 노드가 자기 자신이 되도록 부모 노드 생성
        self.rank = [0] * n # 랭크 리스트 생성 rank는 부분 집합의 크기를 알기 위한 리스트

    def find(self, x): # x의 부모 노드가 뭔지 확인하는 메서드
# 경로 압축 기법 사용
        if self.parent[x] != x: # 인덱스가 자기자신이고 그 인덱스의 원소가 부모 노드
            self.parent[x] = self.find(self.parent[x]) # 계속 위로 가면서 부모 노드가 뭔지 확인
        return self.parent[x] # 부모 노드를 리턴

    def union(self, x, y):
# 두 집합의 루트 노드 찾기
        root_x, root_y = self.find(x), self.find(y) # root_x, root_y에 x, y의 최상위 부모 노드를 할당

# 이미 같은 집합에 속한 경우 합치지 않음
        if root_x == root_y:
            return

# 랭크를 기준으로 작은 트리를 큰 트리에 합침
        if self.rank[root_x] < self.rank[root_y]: # 그 최상위 부모 노드의 집합 크기를 각각 비교해서 작은 트리를 큰 트리의 루트 노드 밑에 합친다.  
            self.parent[root_x] = root_y # 그래서 root_x 의 부모 노드가 root_y가 되는 것
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else: # 두 트리의 크기가 같은 경우 앞의 트리에 포함시키고 그 트리의 크기를 1 늘린다. 
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
# 예시 코드       
def are_friends(uf, x, y):
    return uf.find(x) == uf.find(y)

# 사용 예시
n = 5  # 총 5명의 사람 
uf = UnionFind(n) # parent = [0,1,2,3,4], rank = [0,0,0,0,0] 

uf.union(0, 1)  # 0번과 1번은 친구 # root_0 = 0, root_1 = 1 -> rank[root_0=0] = 0, rank[root_1=1] = 0 -> parent[1] = root_0 = 0, rank[0] = 1 -> 0, 1은 부모 노드로 0을 가진다. parent=[0,0,2,3,4]
uf.union(1, 2)  # 1번과 2번은 친구 # root_1의 경우 find(1)이 parent[1] != 1이므로 parent[1] = find(parent[1] = 0) = 0 return 따라서 root_1 = 0, root_2 = 2이고 rank[0] = 1 > rank[2] = 0 이므로 parent[2] = root_1 = 0  
uf.union(3, 4)  # 3번과 4번은 친구 # root_3 == 3, root_4 == 4 -> rank[root_3==3] == 0, rank[root_4=4] == 0 -> parent[4] = root_3 = 3 rank[3] = 1

print(are_friends(uf, 0, 2))  # True (0번과 2번은 친구)
print(are_friends(uf, 1, 3))  # False (1번과 3번은 친구가 아님)
print(are_friends(uf, 3, 4))  # True (3번과 4번은 친구)   

위 코드에서 `UnionFind` 클래스는 유니온 파인드 자료구조를 구현한 것입니다.

`__init__(self, n)`: 초기화 메서드로, n개의 원소에 대한 유니온 파인드를 초기화합니다. 모든 원소의 부모를 자기 자신으로 설정하고, 랭크를 0으로 초기화합니다.
`find(self, x)`: x가 속한 집합의 대표 원소(루트 노드)를 찾는 연산입니다. 경로 압축 기법을 사용하여 찾은 루트 노드를 x의 부모로 직접 연결함으로써 트리의 높이를 최소화합니다.
`union(self, x, y)`: x가 속한 집합과 y가 속한 집합을 합치는 연산입니다. 먼저 각 원소의 루트 노드를 찾은 후, 랭크가 낮은 트리를 랭크가 높은 트리의 루트 노드에 합칩니다. 만약 랭크가 같다면 한쪽 트리의 랭크를 1 증가시킵니다.

유니온 파인드는 그래프 알고리즘, 특히 최소 신장 트리를 찾는 크루스칼 알고리즘에서 사이클 형성 여부를 판단하는 데 사용됩니다. 또한, 연결성 문제, 그룹 여부 판단 등 다양한 문제에 활용될 수 있습니다.

유니온 파인드의 시간 복잡도는 경로 압축과 랭크를 사용할 경우 거의 상수 시간에 동작하며, 평균적으로 매우 효율적인 자료구조입니다.

위 코드에서 `UnionFind` 클래스는 이전에 설명한 유니온 파인드 구현입니다. `are_friends` 함수는 두 사람이 친구인지 판단하는 함수로, 유니온 파인드의 `find` 연산을 사용하여 두 사람이 같은 집합에 속하는지 확인합니다.
