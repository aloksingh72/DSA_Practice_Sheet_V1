# Dated:- 20/11/2025/Thursday
# Priority Queue using list

class PriorityQueue:
    def __init__(self):
        self.items =[]
    #  method to insert the value in the list
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1]<=priority:
            index +=1
        self.items.insert(index,(data,priority))
    # method to delete the value in the list
    def pop(self):
        