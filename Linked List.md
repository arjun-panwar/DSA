### List - Linear collection of data items
​Example
- List of marks of Test given so far - (int)
- List of cities visited - (str)
- List of Employees - (Employee -class)
In all the above example list I can keep adding list

---
### Node 
 Start [ Data, Address of next]
 ![[Pasted image 20231101194226.png]]
```python 
class Node:
	def __init__(self,item=None,next=None):
		self.item=item
		self.next=next
```
--- 
# Type of Linked List
- [[Singly Linked List]]
- [[Doubly Linked List]]
- [[Circular Linked List]]
- [[Circular Doubly Linked List]]

---
## Checklist for creating any Linked list code 
- [ ] List is empty
- [ ] List just have 1 node
- [ ] List with multiple Node
- [ ] while searching, what if first node match the search data
- [ ] In case of doubly linked list, always take care of next and previous Node 



# Singly Linked List

- SLL is a linear data Structure
- It can grow and Shrink
- It's node contain 
	- item
	- reference of next Node

![[Pasted image 20231101195505.png]]

---

## Operations on Singly Linked List

- Insertion
	- insert at start
	- insert at last
	- insert in between ![[Pasted image 20231101200211.png]]
- Deletion
	- delete start ![[Pasted image 20231101200541.png]]
	- delete last
	- delete between
- Searching
- is_empty
- traverse	

`del keyword just remove reference of the object, it doesn't delete the object`

---
### Code

```python
from node import Node


class SSL:
    def __init__(self, start=None) -> None:
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next=n


    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            temp.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp = self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp = temp.next

    # def __call__(self):
    #     temp = self.start
    #     while temp is not None:
    #         yield temp.item
    #         temp = temp.next
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
mylist = SSL()
print(mylist.is_empty())
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(50)
mylist.insert_at_start(10)
mylist.print_list()
mylist.delete_item(10)
mylist.print_list()

# for i in mylist():
#     print(i)

for i in mylist:
    print(i)

```

---

### Limitations of Singly Linked List 
- We can only go forward
- We can't access previous node
- Last node.next is None, hence wasting memory

--- 
### Performance
- Insertion/Deletion at the start is cheap then Insertion at last - **Traversing required** for  Insertion/Deletion at last




# Doubly Linked List
- Doubly Linked List is a linear data structure
- It's node contain 
	- reference of previous Node
	- item
	- reference of next Node

![[Pasted image 20231102004834.png]]
^9b4z3ix6q5

--- 
### Node
```python
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
```
^2s8c16im0n

---
## Elementary Operations 

- Insertion
	- insert at start
	- insert at last
	- insert in between
- Deletion
	- delete start
	- delete last
	- delete between
- Searching
- is_empty
- traverse	
^x2tkrc2s42
---
### Code for Doubly Linked List

```python 
class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    def insert_at_start(self,data):
        n=Node(item=data,next=self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    def insert_at_last(self, data):
        temp = self.start

        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next

        n= Node(prev=temp,item=data)
        if temp is None:
            self.start=n
        else:
            temp.next =n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(prev=temp,item=data,next=temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
        print()
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def delete_last(self, ):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start

            while temp.next is not None:
                temp = temp.next
            temp.prev.next=None

    def delete_item(self, data):
        
        temp = self.start
        while temp is not None:
            if temp.item==data:

                if temp.next is not None:
                    temp.next.prev=temp.prev

                if temp.prev is not None:
                    temp.prev.next=temp.next
                else:
                    self.start = temp.next
                break
            temp = temp.next
    
    def __iter__(self):
        return DLLIteraror(self.start)
    
class DLLIteraror:
    def __init__(self,start) -> None:
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
for x in mylist:
    print(x,end=' ')
print()
```


## Limitations of Doubly Linked List 
- Last node.next is None, hence wasting memory
^5gy0ttvyfm



# Circular Linked List

- Circular Linked List is a linear data structure
- It's Last node.next = start
---
![[Pasted image 20231103183746.png]] 
*Insertion/Deletion at the start/end is costly Traversing required for both*

--- 

 **Instead of start, use last** 
 ![[Pasted image 20231103013357.png]] 
  - Insertion and deletion in such image![[Pasted image 20231103013702.png]]
### CLL Node
```python 
 class Node:
	def __init__(self,item=None,next=None):
		self.item=item
		self.next=next
```

## Operations on Circular Linked List

- Insertion
	- insert at start
	- insert at last
	- insert in between
- Deletion
	- delete start
	- delete last
	- delete between
- Searching
- is_empty
- traverse	

## Circular Linked List Code

```python 
class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
    
    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next

                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
            
class CLLIterator:
    def __init__(self,start):
        self.current=start 
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        
        return data

cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
# 20 10 50 30 40
for x in cll:
    print(x,end=' ')
print()
cll.print_list()
```

## Circular Doubly Linked List

-  Circular Doubly Linked List is a linear data structure
-  It's node contain 
	- reference of previous Node
	- item
	- reference of next Node
- It's Last node.next = start
![[Pasted image 20231105155719.png]]
### CLL Node

```python
class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
```
## Operations on Circular Linked List

- Insertion
	- insert at start
	- insert at last
	- insert in between
- Deletion
	- delete start
	- delete last
	- delete between
- Searching
- is_empty
- traverse	

## Circular Linked List Code
```python
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
```