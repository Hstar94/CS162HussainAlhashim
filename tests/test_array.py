import unittest
from adts.array import Array


class ArrayTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_initialize(self):
        """
        Test that the initialize method works as expected
        """
        a = Array(10)
        assert len(a) == 10
        a[3] = 5
        b = Array(instance=a)
        assert len(b) == 10

        # exception must be thrown
        with self.assertRaises(TypeError):
            Array(instance=5)

        c = Array()
        assert len(c) == 0

    def test_get_set(self):
        """
        Test that the __getitem__ amd __setitem_ method works as expected
        """
        a = Array(10)
        a[3] = 5
        assert a[3] == 5

        a[4] = 9
        assert a[4] == 9

        a[0] = 1
        assert a[0] == 1

        a[9] = 5
        assert a[9] == 5
        with self.assertRaises(IndexError):
            a[-1] = 4
        with self.assertRaises(IndexError):
            a[10] = 4
        with self.assertRaises(IndexError):
            c = a[-1]
        with self.assertRaises(IndexError):
            d = a[10]

    def test_len_resize(self):
        """
        Test that the len and resize method works as expected
        """
        a = Array(10)
        assert len(a) == 10

        for i in range(len(a)):
            a[i] = i

        a.resize(15)
        for i in range(10):
            assert a[i] == i
        assert len(a) == 15

        for i in range(10, 15):
            assert a[i] == None

    def test_eq(self):
        """
        Test that the eq method works as expected
        """
        a = Array(10)
        b = Array(10)
        c = Array(instance=a)

        assert a == b
        assert a == c

        a[0] = 1
        assert not a == b

        b[0] = 1
        assert a == b

        assert not a == c

        a.resize(15)
        assert not a == b

    def test_iter(self):
        """
        Test that the iter method works as expected
        """
        a = Array(10)

        a[0] = 5
        a[6] = 8
        a[9] = 11
        itr = iter(a)

        assert next(itr) == 5
        assert next(itr) == None
        assert next(itr) == None
        assert next(itr) == None
        assert next(itr) == None
        assert next(itr) == None
        assert next(itr) == 8
        assert next(itr) == None
        assert next(itr) == None
        assert next(itr) == 11

        with self.assertRaises(StopIteration):
            next(itr)

    def test_delitem(self):
        """
        Test that the delitem method works as expected
        """
        a = Array(10)

        a[0] = 5
        a[6] = 8
        assert a[0] == 5
        del a[0]
        assert a[0] == None
        assert a[6] == 8

    def test_clear(self):
        """
        Test that the clear method works as expected
        """
        a = Array(10)

        a[0] = 5
        a[6] = 8
        a[9] = 11
        assert a[0] == 5
        a.clear()

        for i in range(len(a)):
            assert a[i] is None

    def test_str(self):
        """
        Test that the str method works as expected
        """
        a = Array(10)
        assert str(a) == "None None None None None None None None None None "

        a[5] = 99
        assert str(a) == "None None None None None 99 None None None None "

        for i in range(len(a)):
            a[i] = i

        assert str(a) == "0 1 2 3 4 5 6 7 8 9 "

        a.resize(15)

        assert str(a) == "0 1 2 3 4 5 6 7 8 9 None None None None None "

    def test_contains(self):
        """
        Test that the contains method works as expected
        """
        a = Array(10)
        assert 5 not in a

        a[2] = 5

        assert 5 in a

    def test_clone(self):
        """
        Test that the clone method works as expected
        """
        a = Array(10)
        assert Array.clone(a) == a

        with self.assertRaises(TypeError):
            Array.clone(None)


if __name__ == '__main__':
    unittest.main()