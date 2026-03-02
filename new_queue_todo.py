"""
Context:
A queue is appropriate for managing a list of patients in a waiting room for tests,
following First In, First Out (FIFO).

Exercise:
Resolve all TODOs.

Demonstrate how patients are served in the order they arrive.
"""


class NewQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    patient_queue = NewQueue()
    # TODO: Add Patients A, B, and C to the queue (in that order)
    patient_queue.enqueue("Patient A")
    patient_queue.enqueue("Patient B")
    patient_queue.enqueue("Patient C")

    # TODO: The physician is ready to see the first patient in line, get him/her from the queue
    served = patient_queue.dequeue()
    print("Served:", served)  # Patient A
