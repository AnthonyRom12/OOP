class TreeStore:
    def __init__(self):
        self.items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None}
        ]

    def getAll(self):
        return self.items

    def getItem(self, num):
        for i in self.items:
            if i['id'] == num:
                return self.items[num - 1]

    def getChildren(self, key, val):
        for i in self.items:
            d = next(filter(lambda d: d.get(key) == val, self.items), None)
            if d in self.items:
                sp = [d]
                return sp
            if d not in self.items:
                sp = []
                return sp

    def getAllParents(self, key, val):
        for i in self.items:
            d = next(filter(lambda d: d.get(key) == val, self.items), None)
            sp = self.items.index(d, 0)
            sp_1 = self.items[:sp + 1]
            sp_1.reverse()
            return sp_1


ts = TreeStore()

print(ts.getAll())
print(ts.getChildren('id', 4))
print(ts.getChildren('id', 9))
print(ts.getAllParents('id', 7))
