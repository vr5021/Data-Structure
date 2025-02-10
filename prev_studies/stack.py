1. 스택 (Stack) 스택은 후입선출(LIFO: Last-In-First-Out) 원칙을 따르는 자료 구조입니다. 가장 최근에 추가된 데이터가 먼저 나가는 구조입니다.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) # 인스턴스 변수에 item 마지막 인덱스에 추가

    def pop(self):
        if not self.is_empty(): # 인스턴스 변수가 안비어있으면
            return self.items.pop() # 마지막 item 반환하고 지우기

    def is_empty(self): 
        return len(self.items) == 0

    def peek(self): # 인스턴스 변수가 안비어있으면 마지막 인덱스에 있는거 반환
        if not self.is_empty():
            return self.items[-1]

    def __len__(self): # 파이선 내장함수 또는 연산자와 상호작용하여 클래스의 동작을 사용자 정의하므로 던더, 앞뒤로 __가 붙어있다.
    # 단순히 len(self)라 정의하면 오류 일으킴
        return len(self.items)
