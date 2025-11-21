# Dated:- 21/11/2025/Friday

# Implementaion of priority Queue using Linked list


class Node:
    def __init__(self,item = None,priority=None,next = None):
        self.item = item
        self.priority = priority
        self.next = next
    
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def push(self,data,priority):
        n  = Node(data,priority)
        # Case 1: empty list OR insert at start
        if not self.start or priority<self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count +=1

    def is_empty(self):
        return self.start == None
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        data = self.start
        self.start = self.start.next
        self.item_count -=1
        return data.item
    
    def size(self):
        return self.item_count



p1 = PriorityQueue()
p1.push("Amit",4)
p1.push("Rahul",3)
p1.push("Mukul",5)
p1.push("Ajay",2)
p1.push("Rohit",1)
p1.push("Suresh",6)
p1.push("Mirdul",9)

while  not p1.is_empty():
    print(p1.pop())

