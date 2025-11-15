# Date:- 15/11/2025/Saturday
# Queue implementation using the singly linked list


class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next 


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count =0
    def is_empty(self):
        return self.front == None
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear =n
        self.item_count +=1
    def dequeue(self):
        if  self.is_empty():
            raise IndexError("Queue is Empty")
        # when there is only node is present in list
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            # when there is many element present in the list
            self.front = self.front.next
        self.item_count -=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("No data present in the Queue")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("No data is present. ")
    def size(self):
        return self.item_count

q1 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print(q1.get_front(),q1.get_rear())

q1.dequeue()

print(q1.get_front(),q1.get_rear())





