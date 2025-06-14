import unittest
from transaction_test import TestSuite

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
    unittest.TextTestRunner(verbosity=2).run(suite)
