import unittest
from hypothesis import given, strategies
from MyHashSet import MyHashSet


class TestMyHashSetMethods(unittest.TestCase):

    def test_init(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.length, 61)

    def test_hash(self):
        hashset = MyHashSet()
        hash_value = hashset.hash(63)
        self.assertEqual(hash_value, 2)

    def test_add(self):
        hashset = MyHashSet()
        hashset.add(36, 36)
        self.assertEqual(hashset.is_numbers(36), 1)

    def test_remove(self):
        hashset = MyHashSet()
        hashset.add(36, 36)
        hashset.remove(36)
        self.assertEqual(hashset.is_numbers(36), 0)

    def test_get(self):
        hashmap = MyHashSet()
        hashmap.add(1, 1)
        self.assertEqual(hashmap.get(1), 1)

    def test_isNumbers(self):
        hashmap = MyHashSet()
        hashmap.add(1, 1)
        self.assertEqual(hashmap.is_numbers(1), 1)

    def test_size(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.size(), 0)
        hashset.add(36, 36)
        hashset.add(48, 36)
        self.assertEqual(hashset.size(), 2)

    def test_hashSetToDict(self):
        hashset = MyHashSet()
        hashset.add(1, 1)
        hashset.add(2, 2)
        hashset.add(3, 3)
        self.assertEqual(hashset.hashset_to_dict(), {1: 1, 2: 2, 3: 3})

    def test_hashSetToList(self):
        hashset = MyHashSet()
        hashset.add(1, 1)
        hashset.add(2, 2)
        hashset.add(3, 3)
        hashset.add(4, 4)
        self.assertEqual(hashset.hashset_to_list(), [1, 2, 3, 4])

    def test_hashsetfromList(self):
        hashset = MyHashSet()
        list = [1, 2, 3, 4]
        hashset.list_to_hashset(list)
        self.assertEqual(hashset.is_numbers(3), 1)

    def test_filter(self):
        hashset = MyHashSet()
        hashset.add(1, 1)
        hashset.add(2, 2)
        hashset.add(3, 3)
        hashset.add(4, 4)
        hashset.filter(lambda x: x % 2 == 0)
        self.assertEqual(hashset.hashset_to_list(), [2, 4])

    def test_map(self):
        hashset = MyHashSet()
        hashset.add(1, 1)
        hashset.add(2, 2)
        hashset.add(3, 3)
        self.assertEqual(hashset.map(lambda x: x ** 3), [1, 8, 27])

    def test_reduce(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.reduce(lambda a, b: a * b, 1), 1)
        hashset.add(6, 6)
        hashset.add(9, 9)
        self.assertEqual(hashset.reduce(lambda a, b: a * b, 1), 54)

    def test_iter(self):
        hashset = MyHashSet()
        hashset.add(1, 1)
        hashset.add(2, 2)
        hashset.add(3, 3)
        temp = {}
        for e in hashset:
            temp[e.key] = e.value
        self.assertEqual(hashset.hashset_to_dict(), temp)
        i = iter(hashset)
        self.assertEqual(next(i).value, 1)

    def test_associativity_1(self):
        hashset_a = MyHashSet()
        hashset_a.add(1, 1)
        hashset_a.add(2, 2)
        hashset_b = MyHashSet()
        hashset_b.add(3, 3)
        hashset_b.add(4, 4)
        hashset_c = MyHashSet()
        hashset_c.add(5, 5)
        hashset_c.add(6, 6)
        hashset_A = hashset_a
        hashset_B = hashset_b
        hashset_C = hashset_c
        hashset_a.concat(hashset_b)
        hashset_a.concat(hashset_c)
        hashset_A.concat(hashset_C)
        hashset_A.concat(hashset_B)
        self.assertEqual(hashset_a, hashset_A)

    @given(a=strategies.lists(strategies.integers()),
           b=strategies.lists(strategies.integers()),
           c=strategies.lists(strategies.integers()))
    def test_associativity_2(self, a, b, c):
        hashset_a = MyHashSet()
        hashset_b = MyHashSet()
        hashset_c = MyHashSet()
        hashset_a.list_to_hashset(a)
        hashset_b.list_to_hashset(b)
        hashset_c.list_to_hashset(c)
        hashset_A = hashset_a
        hashset_B = hashset_b
        hashset_C = hashset_c
        hashset_a.concat(hashset_b)
        hashset_a.concat(hashset_c)
        hashset_A.concat(hashset_C)
        hashset_A.concat(hashset_B)
        self.assertEqual(hashset_a, hashset_A)

    @given(_list=strategies.lists(strategies.integers()))
    def test_identity(self, _list):
        hashset_a = MyHashSet()
        hashset_b = MyHashSet()
        hashset_a.list_to_hashset(_list)
        self.assertEqual(hashset_a.concat(hashset_b._empty), hashset_a)


if __name__ == '__main__':
    unittest.main(verbosity=2)
