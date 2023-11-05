class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self,start=None) -> None:
        self.start=start
  
    def is_empty(self):
        return self.start is None
    def insert_at_start(self,data):
        n=Node(item=data)
        if self.is_empty():
            self.start =n
            self.start.prev=n
        else:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    
    def insert_at_last(self,data):
        n=Node(item=data)
        if self.is_empty():
            self.start =n
            self.start.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
    def search(self,data):
        temp=self.start
        if temp is None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None

    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(prev=temp,item=data,next=temp.next)
            temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
            while temp is not self.start:
                print(temp.item,end=" ")
                temp=temp.next
                
    def delete_first(self):
        if not self.is_empty():
            if self.start==self.start.next:
                self.start=None
            else:
                self.start.next.prev=self.start.prev
                self.start.prev.next=self.start.next
                self.start=self.start.next
    def delete_last(self):
        if not self.is_empty():
            if self.start==self.start.next:
                self.start=None
            else:
                
                self.start.prev=self.start.prev.prev
                self.start.prev.next=self.start
    def delete_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
                    temp=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data

mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30),35)
mylist.delete_item(20)
for x in mylist:
    print(x,end=' ')

print()

                