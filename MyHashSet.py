"""
The main function module of Hashset, including the init, add,
remove, is_member, size, formList, toList, toNodeList, map,
filter, reduce, empty, _eq_, concat and _iter_ function.
"""


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

    def hash(self, key) -> int:
        hash_value = key % self.length
        return hash_value

    def add(self, value: int) -> None:
        key = value
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

    def remove(self, key: int) -> bool:
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

    def is_member(self, key) -> bool:
        return key in self.keyList

    def size(self) -> int:
        size = len(self.keyList)
        return size

    def fromList(self, lst) -> None:
        self.__init__()
        for value in lst:
            self.add(value)

    def toList(self) -> list:
        lst = []
        if len(self.keyList) == 0:
            return lst
        for i in range(self.length):
            if self.data[i] != self.init:
                head = self.data[i]
                while head is not None:
                    lst.append(head.value)
                    head = head.next
        lst.sort()
        return lst

    def toNodeList(self) -> list:
        nodelist = []
        if len(self.keyList) == 0:
            return nodelist
        for i in range(self.length):
            if self.data[i] != self.init:
                point = self.data[i]
                while point is not None:
                    nodelist.append(point)
                    point = point.next
        return nodelist

    def filter(self, function) -> list:
        lst_res = []
        for value in self.toList():
            if function(value) is True:
                lst_res.append(value)
        return lst_res

    def map(self, function):
        list_src = self.toList()
        for i in range(len(list_src)):
            list_src[i] = function(list_src[i])
        self.fromList(list_src)
        return self

    def reduce(self, func, init_state: int) -> int:
        res = init_state
        it = iter(self)
        for i in it:
            res = func(res, i.value)
        return res

    def __eq__(self, other) -> bool:
        if self.toList() == other.toList():
            return True
        return False

    def empty(self):
        return MyHashSet()

    def concat(self, to_concat):
        if to_concat is None:
            return self
        elif isinstance(to_concat, MyHashSet):
            for key in to_concat.toList():
                self.add(key)
        return self

    def __iter__(self):
        iter_list = self.toNodeList()
        return iter(iter_list)
