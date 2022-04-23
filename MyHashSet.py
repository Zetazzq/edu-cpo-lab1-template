class Node(object):
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashSet(object):
    init = object()

    def __init__(self, dict=None, length=61):
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

    def hashSetToList(self):
        dict = self.hashSetToDict()
        list = []
        for value in dict:
            list.append(value)
        return list

    def filter(self, function):
        for key in self.keyList:
            if (function(key) != 1):
                self.remove(key)
        return self

    def _empty(self):
        return None

    def map(self, function):
        list_in = self.hashSetToList()
        list_out = []
        for value in list_in:
            value = function(value)
            list_out.append(value)
        return list_out

    def reduce(self, func, init_state):
        out = init_state
        for key in self.keyList:
            out = func(out, key)
        return out

    def concat(set1, set2):
        if set1 is None:
            return set2
        elif set2 is MyHashSet:
            for key in set2.keyList:
                value = set2.get(key)
                set1.add(key, value)
                return set1
        return set1

    def __iter__(self):
        iter_list = []
        for key in self.keyList:
            iter_list.append(Node(key, self.get(key)))
        return iter(iter_list)
