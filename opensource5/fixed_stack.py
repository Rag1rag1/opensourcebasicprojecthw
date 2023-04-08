class FixedStack: #FixedStack class 생성
    class Empty(Exception): #Empty class 생성(exception은 예외처리용 내장 class, raise를 사용하기 위함.)
        pass  #아무것도 하지 않는다
    class Full(Exception): #Full class 생성(exception은 예외처리용 내장 class)
        pass  #아무것도 하지 않는다
    def __init__(self, capacity: int = 64) -> None: #__init__ 생성자 선언 (capacity는 default값으로 정수 64를 가짐) 
        self.stk = [None] * capacity #capacity의 크기를 갖는 stk(스택) 리스트 선언
        self.capacity = capacity  #객체 생성시 capacity값에 따라 다른 크기의 스택을 생성.
        self.ptr = 0 #스택 포인터(top을 가리킴) 0으로 초기화

    def __len__(self) -> int: #파이썬 내장 함수 len이 실행될 때 호출되니 메서드
        return self.ptr # ptr의 길이 반환
    def is_empty(self) -> bool:#스택 포인터 ptr이 0이하이면 true 반환
        return self.ptr <= 0
    def is_full(self) -> bool: #self.ptr이 self.capacity보다 크거나 같으면 true 반환  
        return self.ptr >= self.capacity
    def push(self, value: any) -> None:
        if self.is_full(): #self.is_full의 반환갑이 true이면
            raise FixedStack.Full  #FixedStack.Full으로 오류발생.
        self.stk[self.ptr] = value #stk배열의 배열포인터가 가르키는 위치에 value값을 저장 
        self.ptr += 1 #포인터가 가르키는 값 증가
    def pop(self) -> any:#반환값은 뭐든지 가능하다
            if self.is_empty(): #self.is_empty()의 반환값이 true이면
                raise FixedStack.Empty  #FixedStack.Empty으로 오류발생.
            self.ptr -= 1 #포인터가 가르키는 값 감소
            return self.stk[self.ptr] #stk배열의 배열포인터가 가르키는 위치의 값을 반환
    def peek(self) -> any: #변환값 뭐든 가능
        if self.is_empty():
            raise FixedStack.Empty 
        return self.stk[self.ptr - 1]
    def clear(self) -> None:
        self.ptr = 0
    def find(self, value: any) -> int:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
            return -1
    def count(self, value: any) -> int:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
                return c
    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])