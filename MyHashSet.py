import warnings
warnings.filterwarnings("ignore")


class Node(object):
    def __init__(self, key=None, value=None, _next=None):
        self.key = key
        self.value = value
        self.next = _next


class MyHashSet(object):
    init = object()

    def __init__(self, length=61):
        self.keyList = []
        self.data = [self.init for _ in range(length)]
        self.length = length
        self.index = 0

    def hash(self, key):
        hash_value = key % self.length
        return hash_value

    def add(self, key, value):
        hash_value = self.hash(key)
        add_node = Node(key, value)
        if self.data[hash_value] == self.init:
            self.data[hash_value] = add_node
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
            head.next = add_node
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

    def is_numbers(self, key) -> bool:
        return key in self.keyList

    def get(self, key):
        dict = self.hashset_to_dict()
        key = dict[key]
        return key

    def size(self):
        size = len(self.keyList)
        return size

    def list_to_hashset(self, list):
        for key, value in enumerate(list):
            self.add(key, value)

    def dick_to_hashset(self):
        for key, value in dict.items(self):
            self.add(key, value)

    def hashset_to_dict(self):
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

    def hashset_to_list(self):
        dict = self.hashset_to_dict()
        list = []
        for value in dict:
            list.append(value)
        return list

    def filter(self, function):
        for key in self.keyList:
            if function(key) != 1:
                self.remove(key)
        return self

    def map(self, function):
        list_in = self.hashset_to_list()
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

    def _empty(self):
        return None

    def concat(self, set):
        if self is None:
            return set
        elif set is MyHashSet:
            for key in set.keyList:
                value = set.get(key)
                self.add(key, value)
                return self
        return self

    def __iter__(self):
        iter_list = []
        for key in self.keyList:
            iter_list.append(Node(key, self.get(key)))
        return iter(iter_list)
