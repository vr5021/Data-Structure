# 최단 경로 문제
각 간선의 가중치 합이 최소가 되는 두 정점(또는 노드) 사이의 경로를 찾는 문제 
  -  교차로: 정점(vertex)
  -  길: 간선(edge)
  -  거리, 시간: 가중치(weight)
  -  그래프의 종류와 특성에 따라 각각 최적화된 다양한 최단 경로 알고리즘이 존재 ex. Dijkstra
## 다익스트라 알고리즘
  - 항상 노드 주변의 최단 경로만을 택하는 대표적인 Greedy 알고리즘 중 하나.
  - 노드 주변을 탐색할 때 BFS를 이용하는 대표적인 알고리즘
  - 가중치가 음수인 경우는 처리 불가능. 임의의 정점을 출발 집합에 더할 때, 그 정점까지의 최단거리는 계산이 끝났다는 확신을 갖고 더한다.
  - 우선순위 큐를 적용하면 O(V+E), 모든 정점이 출발지에서 도달이 가능할 경우 최종적으로 O(ElogV).

# [네트워크 딜레이 타임](https://leetcode.com/prblems/network-delay-time/)
K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다.            
입력값 (u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.
  - 풀이 1 다익스트라 알고리즘 구현
    - 가장 오래 걸리는 노드까지의 최단 시간 판별 -> 다익스트라 알고리즘으로 추출
    - 모든 노드에 도달할 수 있는지 여부 판별 -> 모든 노드의 다익스트라 알고리즘 계산 값이 존재하는지 유무로 판별
    - 우선 순위 큐를 이용한 다익스트라 알고리즘 구현
      ```pseudocode
      function Dijkstra(Graph, source):
        create vertex priority queue Q
        
        dist[source] ← 0                          // Initialization
        Q.add_with_priority(source, 0)            // associated priority equals dist[·]
        
        for each vertex v in Graph.Vertices:
           if v ≠ source
              prev[v] ← UNDEFINED               // Predecessor of v
              dist[v] ← INFINITY                // Unknown distance from source to v
           Q.add_with_priority(v, dist[v])      # 각 정점과 거리를 우선순위 큐에 삽입
        
        
        while Q is not empty:                     // The main loop
          u ← Q.extract_min()                   // 우선순위 큐에서 최소 값 추출
          for each neighbor v of u:             // 이웃 살펴보기
              alt ← dist[u] + Graph.Edges(u, v)
              if alt < dist[v]:
                  prev[v] ← u
                  dist[v] ← alt
                  Q.decrease_priority(v, alt)
        
        return dist, prev
      ```
    - 큐 변수 Q는 (소요 시간, 정점) 구조로 구성. 시작점에서 정점까지의 소요 시간을 담아둠
    - heapq 모듈은 우선순위를 조정하는 기능을 지원하지 않으므로 decrease_priority() 부분을 추출한
      노드가 dist에 없으면 dist에 push하는 형태로하여 dist에는 항상 최솟값이 셋팅되는 형식으로 수정한다.
    ```python3
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
      graph = collection.defaultdict(list)
      # 그래프 인접 리스트 구성
      for u, v, w in times:
        graph[u].append((v, w))
    
      # 큐 변수 : [(소요 시간, 정점)]
      Q = [(0, k)]
      dist = collection.defaultdict(int)
    
      # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
      while Q:
        time, node = heapq.heappop(Q) # 현재까지 가장 짧은 거리의 노드 선택, 현재 노드가 node로 되고 여기의 인접 노드 탐색, 현재 노드까지의 비용이 time
    
        if node not in dist: # 있으면 그냥 넘어가고 dist에 추가x
          dist[node] = time
          for v, w in graph[node]: # 현재 노드에서 갈 수 있는 모든 인접 노드 탐색
            alt = time + w
            heapq.heappush(Q, (alt, v))
    
      # 모든 노드의 최단 경로 존재 여부 판별
      if len(dist) == n:
        return max(dist.values())
      return -1
      ```

# [K 경유지 내 가장 저렴한 항공권](https://leetcode.com/prblems/cheapest-flight-within-k-stops/)
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라.        
경로가 존재하지 않을 경우 -1을 리턴한다.    
  - 풀이 1 다익스트라 알고리즘 응용
    - 가격을 시간이라 가정하여 다익스트라 적용
    - 우선순위 큐에 추가할 때 K 이내일 때만 경로를 추가하여 K를 넘어서는 경로는 더 이상 탐색되지 않도록 한다.
    ```python3
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
      graph = collections.defaultdict(list)
      # 그래프 인접 리스트 구성
      for u, v, w in flights:
        graph[u].append((v, w))
    
      # 큐 변수: [(가격, 정점, 남은 간으 경유지 수)]
      Q = [(0, src, K)]
    
      # 우선순위 큐 최솟값 기준으로 도착점까지 최단 비용 판별
      while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
          return price
        if k >= 0:
          for v, w in graph[node]:
            alt = price + w
            heapq.heappush(Q, (alt, v, k - 1))
    
      return -1
    ```
