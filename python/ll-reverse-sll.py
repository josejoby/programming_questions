"""
Reverse a Singly Linked List 
"""


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next_element = None
    def __str__(self) -> str:
        return f"[{self.data}]"

class LinkedList:

    def __init__(self) -> None:
        self.head_node = None

    def get_head(self):
        return self.head_node
    
    def insert_node(self, node) -> None:
        if self.head_node is None:
            self.head_node = node
        else:
            curr_node = self.head_node
            while curr_node.next_element:
                curr_node = curr_node.next_element
            curr_node.next_element = node
        return
    
    def __str__(self): # for printing
        node = self.head_node
        s=None
        while node:
            s = f"{s}->{node.data}" if s else f"{node.data}"
            node = node.next_element
        s = f"{s}->None"
        return s


def reverse(lst):
    node = lst.get_head()
    prev_node = None
    while node:
        next_node = node.next_element
        node.next_element = prev_node
        prev_node = node
        node = next_node
        ll.head_node = prev_node

if __name__ == '__main__':
    data = [10,9,4,6]
    # creating a sll
    ll = LinkedList()
    for v in data:
        ll.insert_node(Node(v))
    print(ll)
    
    reverse(ll)
    print(ll)
