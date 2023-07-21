import calc
import operations
import unittest


class TestOperations(unittest.TestCase):

    def test_add(self):
        # test basic addition
        self.assertEqual(operations.add(3, 5))



    def test_subtract(self):

        self.assertEqual(operations.subtract(8, 4), 2)




    def test_invalid_input(self):

        with self.assertRaises(TypeError):
            operations.add('2', 3)


        with self.assertRaises(TypeError):
            operations.subtract('5', 3)
