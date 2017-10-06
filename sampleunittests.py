# pip install mock
# python sampleunittests.py

from unittest import TestCase, main
from mock import patch


# Test Functions and Classes
def _mock_test_func(value):
    return value + 2


def _test_func_one(value):
    return value + 1


def _test_func_two(value):
    return value * 2


class TestClass(object):
    def __init__(self):
        self.number = 0


# Sample Tests
class SampleTests(TestCase):
    """
    Basic Example Tests
    """

    def setUp(self):
        """ Common Setup For All Tests - Runs before each test """
        self.obj1 = TestClass()
        self.obj2 = TestClass()

    # Not used in this example
    # def tearDown(self):
    #     """ Common Tear Down For All Tests - Runs after each test """

    def test_basic_asserts(self):
        """ Demonstrates how to use basic asserts """
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIs(self.obj1, self.obj1)
        self.assertIsNot(self.obj1, self.obj2)
        self.assertIsNone(None)
        self.assertIsNotNone(1)
        self.assertIn(1, [1, 2])
        self.assertNotIn(1, [2, 3])
        self.assertIsInstance('1', str)
        self.assertNotIsInstance(1, str)

    def test_exception(self):
        """ Demonstrates how to test exceptions """
        # Test an exception is raised
        with self.assertRaises(Exception):
            raise Exception

        # Test that an exception is not raised
        try:
            a = 1 + 1
        except Exception as e:
            self.fail("Test failed due to exception %s" % str(e))


    @patch('__main__._test_func_two', _mock_test_func)
    @patch('__main__._test_func_one')
    def test_mock(self, mock1):
        """ Demonstrates how basic mocking works """
        _test_func_one(1)
        _test_func_one(3)

        self.assertTrue(mock1.called)
        self.assertEqual(mock1.call_count, 2)

        # Uses the mocked function (would equal 2 otherwise)
        response = _test_func_two(1)
        self.assertEqual(response, 3)


if __name__ == '__main__':
    main()
