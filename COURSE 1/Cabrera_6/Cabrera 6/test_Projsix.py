
import Projsix
from Projsix import *
from Projsix import Deque
import unittest

deq = Deque()

class TestPS(unittest.TestCase):

    def test_displayQ(self):
        if deq.displayQ == Deque:
            self.assertTrue

    def test_addfrontQ(self):
        if deq.addfrontQ(5) == deq.pfront():
            self.assertTrue

    def test_addbackQ(self):
        self.assertEqual(deq.addbackQ(5), deq.pback())




unittest.main()