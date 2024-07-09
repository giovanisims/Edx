class Jar:
    def __init__(self, capacity=12,size=0,n=0):
        self.capacity = capacity
        self.size = size
        self.n = n

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        if size < 0:
            raise ValueError
        self._size = size


jar = Jar()
print(jar)
print(jar.capacity)
print(jar.size)
jar.deposit(5)
jar.withdraw(2)
print(jar)