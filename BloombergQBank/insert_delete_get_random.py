class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.list.append(val)
        self.dict[val] = len(self.list)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_elem,

    def getRandom(self) -> int:
