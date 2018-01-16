import unittest


class SequenceTest(unittest.TestCase):
    def test_assign_to_slice(self):
        l = list(range(10))
        l[2:5] = [20, 30]
        self.assertEqual([20, 30], l[2:4])

        del l[5:7]
        self.assertEqual([0, 1, 20, 30, 5, 8, 9], l)

        l[3::2] = [11, 22]
        self.assertEqual([0, 1, 20, 11, 5, 22, 9], l)

    def test_sorted(self):
        fruits = ['grape', 'raspberry', 'apple', 'banana']
        sorted_fruits = sorted(fruits)
        self.assertEqual(['apple', 'banana', 'grape', 'raspberry'], sorted_fruits)

        rev_sorted = sorted(fruits, reverse=True)
        self.assertEqual(['raspberry','grape','banana','apple'],rev_sorted)

        len_sorted = sorted(fruits,key=len)
        self.assertEqual(['grape','apple','banana','raspberry'],len_sorted)
