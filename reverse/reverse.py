class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f"Value: {self.value} ->(Next: {self.next_node}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # prev = None
        # current = self.head
        # while current is not None:
        #     print('*******************************')
        #     print(f'Current Node: {current}')
        #     next = current.next_node
        #     print(f'Next Node: {next}')
        #     current.next = prev
        #     print(f"Current Node's Previous Node set to: {prev}")
        #     prev = current
        #     print(f"Setting prev to current...")
        #     current = next
        #     print(f"Setting current to next...\n\n")
        # self.head = prev

        # If last node mark it head
        if self.head is not None:
            if node.get_next() is None:
                self.head = node

                # Update next to prev node
                node.set_next(prev)
                return

            # Save curr.next node for recursive call
            next = node.get_next()

            # And update next
            node.set_next(prev)

            self.reverse_list(next, node)
