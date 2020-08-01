class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.currentOldest = 0

    def incOldest(self):
        if self.currentOldest == self.capacity - 1:
            self.currentOldest = 0
        else:
            self.currentOldest += 1

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.currentOldest] = item
            self.incOldest()
        else:
            self.storage.append(item)
            self.incOldest()

    def get(self):
        return self.storage
