"""
Context:
A hospital wants to store a dynamically changing list of patients awaiting lab results.
A linked list structure allows easy insertion/removal without contiguous memory.

Exercise:
Resolve all TODOs.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, item):
        current = self.head
        prev = None
        while current:
            if current.data == item:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def display(self):
        current = self.head
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        print(" -> ".join(items))


if __name__ == "__main__":
    patient_list = LinkedList()
    # TODO: Fill in the linked list with patients so it displays 'Patient A -> Patient B -> Patient C'
    patient_list.append("Patient A")
    patient_list.append("Patient B")
    patient_list.append("Patient C")
    patient_list.display()  # Patient A -> Patient B -> Patient C

    # TODO: Adjust the linked list so it displays 'Patient A -> Patient C'
    patient_list.remove("Patient B")
    patient_list.display()  # Patient A -> Patient C
