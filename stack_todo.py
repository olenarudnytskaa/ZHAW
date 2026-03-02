"""
Context:
In a medical software system, a stack could track a series of "undo" operations for
changes to patient records—Last In, First Out (LIFO).

Exercise:
Implement a Stack class with:
- push(item)
- pop()
- is_empty()

Demonstrate how you might record edits and then pop the most recent edit for an undo.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    edit_stack = Stack()
    edit_stack.push("Edit1: Added new lab result") # TODO: Add the string "Edit1: Added new lab result" to the stack
    edit_stack.push("Edit2: Changed dosage info") # TODO: Add the string "Edit2: Changed dosage info" to the stack

    last_edit = edit_stack.pop() # TODO: Remove the last edit from the stack and assign it to 'last_edit' simulating an undo operation
    print("Undo operation:", last_edit)
