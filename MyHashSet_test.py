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
        hashset.add(36)
        self.assertEqual(hashset.is_member(36), True)

    def test_remove(self):
        hashset = MyHashSet()
        hashset.add(36)
        hashset.remove(36)
        self.assertEqual(hashset.is_member(36), False)

    def test_isNumbers(self):
        hashmap = MyHashSet()
        hashmap.add(1, 1)
        self.assertEqual(hashmap.is_member(1), 1)

    def test_hashsetfromList(self):
        a = MyHashSet()
        lst = [1, 2, 3, 4]
        a.list_to_hashset(lst)
        b = MyHashSet()
        b.add(1)
        b.add(2)
        b.add(3)
        self.assertEqual(a, b)

    def test_size(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.size(), 0)
        hashset.list_to_hashset([36, 48])
        self.assertEqual(hashset.size(), 2)

    def test_hashSetToList(self):
        hashset = MyHashSet()
        hashset.list_to_hashset[4, 2, 3, 1]
        self.assertEqual(hashset.hashset_to_list(), [1, 2, 3, 4])

    def test_filter(self):
        hashset = MyHashSet()
        hashset.list_to_hashset([2, 3, 1, 4])
        hashset.filter(lambda x: x % 2 == 0)
        self.assertEqual(hashset.hashset_to_list(), [2, 4])

    def test_map(self):
        hashset = MyHashSet()
        hashset.list_to_hashset([2, 3, 1])
        self.assertEqual(hashset.map(lambda x: x ** 3), [1, 8, 27])

    def test_reduce(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.reduce(lambda a, b: a * b, 1), 1)
        hashset.add(6)
        hashset.add(9)
        self.assertEqual(hashset.reduce(lambda a, b: a * b, 1), 54)

    def test_iter(self):
        x = [1, 2, 3]
        hashset = MyHashSet()
        hashset.list_to_hashset(x)
        tmp = []
        for e in hashset:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(hashset.to_list(), tmp)
        i = iter(MyHashSet())
        self.assertRaises(StopIteration, lambda: next(i))

    @given(a=strategies.lists(strategies.integers()),
           b=strategies.lists(strategies.integers()),
           c=strategies.lists(strategies.integers()))
    def test_associativity(self, a, b, c):
        hashset_a = MyHashSet()
        hashset_b = MyHashSet()
        hashset_c = MyHashSet()
        hashset_A = MyHashSet()
        hashset_B = MyHashSet()
        hashset_C = MyHashSet()
        hashset_a.list_to_hashset(a)
        hashset_b.list_to_hashset(b)
        hashset_c.list_to_hashset(c)
        hashset_A.list_to_hashset(a)
        hashset_B.list_to_hashset(b)
        hashset_C.list_to_hashset(c)
        hashset_a.concat(hashset_b)
        hashset_a.concat(hashset_c)
        hashset_B.concat(hashset_C)
        hashset_A.concat(hashset_B)
        self.assertEqual(hashset_a, hashset_A)

    @given(_list=strategies.lists(strategies.integers()))
    def test_empty(self, _list):
        hashset_a = MyHashSet()
        hashset_a.list_to_hashset(_list)
        self.assertEqual(hashset_a.concat(hashset_a._empty), hashset_a)
        self.assertEqual(hashset_a, hashset_a.concat(hashset_a._empty))


if __name__ == '__main__':
    unittest.main(verbosity=2)
