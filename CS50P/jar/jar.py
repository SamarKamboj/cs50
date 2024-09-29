class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookie = 0

    def __str__(self):
        return "\U0001F36A" * self.size

    def deposit(self, n):
        self.cookie += n
        if self.cookie > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.cookie -= n
        if self.cookie < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.cookie
