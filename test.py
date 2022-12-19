import unittest
import unionfind


class UnionFindTest(unittest.TestCase):

    def setUp(self):
        self.forest = unionfind.unionfind(10)

    def test_basic(self):
        for i in range(10):
            self.assertEqual(self.forest.find(i), i)

        self.forest.unite(1,2)
        self.assertEqual(self.forest.find(1), self.forest.find(2))
        #self.assertEqual(self.forest.n_sets, 9)

        self.forest.unite(2,3)
        self.forest.unite(3,4)
        for i in range(5, 10):
            self.assertNotEqual(self.forest.find(1), self.forest.find(i))

        self.forest.unite(5,6)
        self.forest.unite(6,7)
        self.forest.unite(7,8)
        self.forest.unite(8,9)
        #self.assertEqual(self.forest.n_sets, 3)

        self.forest.unite(0,9)
        #self.assertEqual(self.forest.n_sets, 2)
        self.assertEqual(self.forest.find(9), self.forest.find(0))
        self.assertNotEqual(self.forest.find(9), self.forest.find(1))
        print(self.forest.groups())

if __name__ == "__main__":
    unittest.main()
