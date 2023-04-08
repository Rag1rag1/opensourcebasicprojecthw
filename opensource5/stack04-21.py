def deque(self) -> Any:
    if self.is_empty():
        raise FixedQueue.Empty
    x=self.que[self.front]
    self.front+=1
    self.no-=1
    if self.front==self.capacity:
        self.front=0
    return x
def peek(self)->Any:

    if self.is_empty():
        raise FixedQueue.Empty
    return self.que[self.front]

def find(self,value: Any)->Any:

    for i in range(self.no):
        idx=(i+self.front)%self.capacity
        if self.que[idx]==value:
            return idx
        return -1
def count(self,value: Any)->bool:
    c=0
    for i in range(self.no):
        idx=(i+self.front)%self.capacity
        if self.que[idx]==value:
            c+=1
    return c
def __contains__(self,value: Any)->bool:
    return self.count(value)
def clear(self)->None:
    self.no =self.front=self.rear=0

def dump(self)->None:
    if self.is_empty():
        print("큐가 비었습니다.")
    else:
        for i in range(self.no):
            print(self.que[(i+self.front)%self.capacity],end='')
        print()
