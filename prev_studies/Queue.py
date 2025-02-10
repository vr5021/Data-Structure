1. 큐 (Queue) 큐(줄서기)는 선입선출(FIFO: First-In-First-Out) 원칙을 따르는 자료 구조입니다. 처음 들어온 데이터가 먼저 나가는 구조입니다.

 class Queue:
  def __init__(self):
      self.items = [] # class 내 items 인스턴스 변수화(field), 이 클래스로 인스턴스를 생성할 때 자기만의 items 리스트를 만들어내 클래스 내에 있는 다른 메서드(enqueue, dequeue, is_empty...)에서 이 인스턴스에 대한 작업을 할 수있게 한다.

  def enqueue(self, item):
      self.items.append(item) # self.items라는 인스턴스 변수에 리스트의 마지막에 추가

  def dequeue(self):
      if not self.is_empty(): # instance가 비어있지않으면 
          return self.items.pop(0) # 리스트의 첫번째를 반환하고 지운다. 

  def is_empty(self): #instance 변수가 비어 있으면 true
      return len(self.items) == 0 

  def peek(self):
      if not self.is_empty(): # instance 변수가 비어있지않으면
          return self.items[0] # 가장 먼저 들어온 아이템 확인

  def __len__(self):
      return len(self.items) # 인스턴스 변수 길이확인
