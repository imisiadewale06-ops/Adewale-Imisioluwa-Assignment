#diagram
#head -> 5 -> 10 -> 20 -> 30 -> None

#---
# Define a Node class using Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a new node at the head
def insert_at_head(head, new_data):
    new_node = Node(new_data)  # Step 1: create new node
    new_node.next = head       # Step 2: point to current head
    head = new_node            # Step 3: update head
    return head

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original list:")
print_list(head)

head = insert_at_head(head, 5)

print("After inserting 5 at the head:")
print_list(head)
