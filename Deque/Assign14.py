# Dated:- 16/11/2025/Sunday
# Deque implementation using the list

class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self,data):
        self.items.insert(0,data)

    def insert_rear(self,data):
        self.items.append(data) # append put the element at the last


    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is empty")
    
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop(-1)
        else:
            raise IndexError("Deque is empty")
        
    def  get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[0]
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    


d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_front(40)
d1.insert_rear(50)
d1.insert_rear(60)
d1.insert_rear(70)

print(d1.get_front(),d1.get_rear())

print(d1.size())




