class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(delete_me):
    if delete_me.next:
        next_node = delete_me.next
        delete_me.data = next_node.data
        delete_me.next = next_node.next
    else:
        raise Exception("can't delete the last node using this method")

def print_linkedlist(head):
    current = head
    print(current.data)
    while current.next:
        current = current.next
        print(current.data)

# TEST
a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
a.next = b
b.next = c
c.next = d
d.next = e

print_linkedlist(a)
delete_node(d)
print("after delete ---")
print_linkedlist(a)

    
