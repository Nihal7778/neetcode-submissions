class MyHashSet:

    def __init__(self):
        self.data=[]
        

    def add(self, key: int) -> None:
        for num in self.data:
            if num == key:
                return

        self.data.append(key)
        

    def remove(self, key: int) -> None:
        for i in range(len(self.data)):
            if self.data[i]==key:

                self.data.pop(i)
                return

        

    def contains(self, key: int) -> bool:
        for num in self.data:
            if num ==key:
                return True

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)