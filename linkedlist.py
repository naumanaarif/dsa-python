class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data: any) -> None:
        """Insert an element at the beginning of a LinkedList"""
        if type(data) in [list, tuple, set]:
            for item in data:
                node = Node(item, self.head)
                self.head = node
            return

        node = Node(data, self.head)
        self.head = node

    def push(self, data: any) -> None:
        """Push an element at the end of a LinkedList"""
        if not self.head:
            self.head = Node(data)
            return
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        cursor.next = Node(data)

    def __str__(self) -> None:
        """Print a LinkedList object."""
        if not self.head:
            return "An empty Linked List."

        cursor = self.head
        ll_str = ""
        while cursor:
            ll_str += str(cursor.data) + " -> "
            cursor = cursor.next
        return ll_str

    @classmethod
    def to_LinkedList(cls, seq: list):
        llist = LinkedList()
        for data in seq:
            llist.push(data)
        return llist


if __name__ == "__main__":
    llist = LinkedList()
    print(llist)
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    print(llist)
    # llist.push(4)
    # print(llist)
    llist.insert([4, 5, 6])
    print(llist)
