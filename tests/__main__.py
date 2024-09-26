import unittest

if __name__ == '__main__':
    test_utils = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test_utils)
