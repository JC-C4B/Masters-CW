import unittest
import Project_3_code
from Project_3_code import isGameOver
from Project_3_code import shipC
from Project_3_code import setupBoard
from Project_3_code import guess_grid
from Project_3_code import checkHitOrMiss

#Make test class:
class TestIGO(unittest.TestCase):
    
    #Check if isGameOver returns True
    def test_isGameOvertrue(self):
        if isGameOver() == True:
            self.assertTrue(isGameOver)
    
    #Check if isGameOver returns False
    def test_isGameOverfalse(self):   
        if isGameOver() == False:
            self.assertFalse(isGameOver)
    
    #Check if there are 5 ships
    def test_setupBoardships(self):
        if (" X ") in guess_grid == 5:
            self.assertTrue(setupBoard)
    
    #Check if the remaining 35 spaces are not ships
    def test_setupBoardfree(self):
        if (" . ") in guess_grid == 35:
            self.assertTrue(setupBoard)
    
    #Test for a HIT
    def test_checkHitOrMissHIT(self):
        if print() == "HIT!":
            self.assertTrue(checkHitOrMiss)
    
    #Test for a MISS
    def test_checkHitOrMissMISS(self):
        if print() == "MISS!":
            self.assertFalse(checkHitOrMiss)

#Run main
if __name__ == "__main__":
    unittest.main



