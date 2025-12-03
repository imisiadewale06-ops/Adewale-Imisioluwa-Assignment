#Create a class node and linked list
# Node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Node with value {key} not found.")
            return

        prev.next = temp.next
        temp = None

    # Display the linked list
    def display_list(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.display_list()   # Output: 5 -> 10 -> 20 -> 30 -> None
    ll.delete_node(20)
    ll.display_list()   # Output: 5 -> 10 -> 30 -> None
    ll.delete_node(100) # Output: Node with value 100 not found.
