import unittest
from hypothesis import given, strategies
from MyHashSet import *


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
        self.assertEqual(hashset.isNumbers(36), 1)

    def test_remove(self):
        hashset = MyHashSet()
        hashset.add(36, 36)
        hashset.remove(36)
        self.assertEqual(hashset.isNumbers(36), 0)

    def test_size(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.size(), 0)
        hashset.add(36, 36)
        hashset.add(48, 36)
        self.assertEqual(hashset.size(), 2)

    def test_filtereven(self):
        hashmap = MyHashSet()
        hashmap.listToHashSet([1, 6, 3, 12])
        self.assertEqual(hashmap.filterEven(), [1, 3])

    def test_hashSetToDict(self):
        hashset = MyHashSet()
        hashset.add(1, 1)
        hashset.add(2, 2)
        hashset.add(3, 3)
        self.assertEqual(hashset.hashSetToDict(), {1: 1, 2: 2, 3: 3})

    def test_reduce(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.reduce(lambda a, b: a * b, 1), 1)
        hashset.add(6, 6)
        hashset.add(9, 9)
        self.assertEqual(hashset.reduce(lambda a, b: a * b, 1), 54)

    def test_concat(self):
        hashset_a = MyHashSet()
        hashset_a.add(1, 1)
        hashset_a.add(2, 2)
        hashset_b = MyHashSet()
        hashset_b.add(3, 3)
        hashset_b.add(4, 4)
        hashset_c = MyHashSet()
        hashset_c.add(5, 5)
        hashset_c.add(6, 6)
        ab = MyHashSet()
        ab_c = MyHashSet()
        bc = MyHashSet()
        bc_a = MyHashSet()
        ab.concat(hashset_a, hashset_b)
        ab_c.concat(ab, hashset_c)
        bc.concat(hashset_b, hashset_c)
        bc_a.concat(bc, hashset_a)
        self.assertEqual(ab_c.hashSetToDict(), bc_a.hashSetToDict())

    # @given(strategies.lists(strategies.integers()))
    # def test_Identity(self, temp):
    #     hash1 = MyHashSet()
    #     hash2 = MyHashSet()
    #     hash1.listToHashSet(temp)
    #     self.assertEqual(hash1.concat(hash2.empty(), hash1), hash1)
    #     self.assertEqual(hash1.concat(hash1, hash2.empty()), hash1)


if __name__ == '__main__':

    unittest.main(verbosity=2)
