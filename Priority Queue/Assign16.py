# Dated:- 20/11/2025/Thursday
# Priority Queue using list
#  there are 4 operations in Priority Queue
# --->push()
# ---->pop()
# ---->is_empty()
# ---->size()


class PriorityQueue:
    def __init__(self):
        self.items =[]
    #  method to insert the value in the list
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1]<=priority:
            index +=1
        self.items.insert(index,(data,priority))
    # to check the list is empty
    def is_empty(self):
         return  len(self.items)==0
    
    # method to delete the value in the list
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)


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


