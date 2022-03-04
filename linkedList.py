class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def equals(self,x):
        if(self.value == x.value): return True
        return False
    def compareTo(self,x):
        if(self.value>x.value):return 1
        elif(self.value<x.value):return -1
        else: return 0

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add(self,x):
        newNode = Node(x)
        if(not self.head):
            self.head = newNode
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode
        self.length += 1

    def addFirst(self,x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
    
    def remove(self,n):
        if(n>self.length-1): n=self.length-1
        temp = self.head
        if(n==0):
            self.head = self.head.next
            self.length-=1
            return temp
        prev = temp
        for i in range(0,n):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        self.length-=1
        return temp

    def get(self,n):
        if(n>self.length-1): n=self.length-1
        if(n==0):
            return self.head
        temp = self.head
        for i in range(0,n):
            temp = temp.next
        return temp

    def reverse(self):
        temp = self.head
        nexty = temp.next
        prev = temp.next
        while(prev):
            nexty = prev.next
            prev.next = temp
            temp = prev
            prev = nexty
        self.head.next = None
        self.head = temp
        return self

    def copy(self):
        newList = LinkedList()
        temp = self.head
        while(temp):
            newList.add(temp.value)
            temp = temp.next
        return newList

    def increment(self,node):
        if(node==self.head):
            temp = self.head.next
            self.head.next = temp.next
            temp.next = self.head
            self.head = temp
        else:
            prev = self.head
            while(prev):
                if(prev.next==node):break
                prev = prev.next
            nexty = node.next
            prev.next = nexty
            node.next = nexty.next
            nexty.next = node
        
    def sort(self):
        node = self.head
        while(node):
            temp = node
            nexty = temp.next
            while(temp.next):
                if(temp.compareTo(temp.next)>0):
                    self.increment(temp)
            node = node.next


    def print(self):
        if(not self.head):
            print("empty!")
            return None
        temp = self.head
        while(temp):
            print(temp.value, end=" ")
            temp = temp.next

list = LinkedList()
list.add("c")
list.add("b")
list.add("a")
list.add("d")
list.print()
list.sort()
list.print()