
class LinkedList:
    def __init__(self):
        self.head = None

    def kth_from_end(self, k):
        if not self.head:
            raise Exception("LinkedList is empty.")

        slow = self.head
        fast = self.head

        # Move the fast pointer k nodes ahead of the slow pointer.
        for i in range(k):
            if not fast:
                raise Exception(f"LinkedList has less than {k} nodes.")
            fast = fast.next

        # Move the slow and fast pointers together until the fast pointer
        # reaches the end of the linked list.
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.val
