
import PFC
from PFC import *
import unittest

class Test_test1(unittest.TestCase):
    
    def Test_Perimeter(self):
        if Rectangle.Perimeter() == 2*eval(self.Length) + 2*eval(self.Width):
            self.assertTrue(self)

    def Test_Area(self):
        if Rectangle.Area() == return eval(self.Length) * eval(self.Width):
            self.assertTrue(self)

    def Test_Volume(self):
        if Parallelepiped(REctangle).Volume() == eval(self.Length) * eval(self.Width) * eval(self.Height):
            self.assertTrue(self)