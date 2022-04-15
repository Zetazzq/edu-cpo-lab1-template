from multiprocessing.sharedctypes import Value
from tempfile import tempdir


class Node(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashSet(object):
    init = object()

    def __init__(self, dict=None, length=61):
        if dict is not None:
            self.hashSetFromDict(self, dict)

        self.keyList = []
        self.data = [self.init for i in range(length)]
        self.length = length
        self.index = 0

    def hash(self, key):
        hash_value = key % self.length
        return hash_value

    def add(self, key, value):
        hash_value = self.hash(key)
        addNode = Node(key, value)
        if self.data[hash_value] == self.init:
            self.data[hash_value] = addNode
            self.keyList.append(key)
        else:
            head = self.data[hash_value]
            while head.next is not None:
                if head.key == key:
                    head.value = value
                    return
                head = head.next
            if head.key == key:
                head.value = value
                return
            head.next = addNode
            self.keyList.append(key)
        return

    def remove(self, key):
        hash_value = self.hash(key)
        if self.data[hash_value] is self.init:
            return False
        elif self.data[hash_value].key is key:
            self.data[hash_value] = self.data[hash_value].next
            self.keyList.remove(key)
            return True
        p = self.data[hash_value]
        q = self.data[hash_value].next
        while q.next is not None:
            if q.key == key:
                p.next = q.next
                self.keyList.remove(key)
                return True
            p = q
            q = q.next
        if q.key == key:
            p.next = None
            self.keyList.remove(key)
            return True

    def isNumbers(self, key) -> bool:
        return key in self.keyList

    def get(self, key):
        dict = self.hashSetToDict()
        key = dict[key]
        return key

    def size(self):
        size = len(self.keyList)
        return size

    def listToHashSet(self, list):
        for key, value in enumerate(list):
            self.add(key, value)

    def dickToHashSet(self):
        for key, value in dict.items():
            self.add(key, value)

    def hashSetToDict(self):
        dict = {}
        if len(self.keyList) == 0:
            return dict
        for i in range(self.length):
            if self.data[i] != self.init:
                head = self.data[i]
                while head is not None:
                    dict[head.key] = head.value
                    head = head.next
        return dict

    def hashSatToList(self):
        dict = self.hashSetToDict()
        list = []
        for value in dict:
            list.append(value)
        return list

    def findEven(self):
        dict = self.hashSetToDict()
        list = []
        for value in dict.items():
            if value % 2 == 0:
                list.append(value)
        return

    def filterEven(self):
        list = self.hashSatToList()
        temp = []
        for value in list:
            if value % 2 != 0:
                temp.append(value)
        return temp

    def reduce(self, func, init_state):
        out = init_state
        for key in self.keyList:
            out = func(out, key)
        return out

    def concat(self, a, b):
        if a is None:
            if b is None:
                return 0
            else:
                for key in b.keyList:
                    self.add(key, key)
        if b is None:
            if a is None:
                return 0
            else:
                for key in a.keyList:
                    self.add(key, key)
        for key in a.keyList:
            self.add(key, key)
        for key in b.keyList:
            self.add(key, key)
        return self

    def empty(self):
        return None
