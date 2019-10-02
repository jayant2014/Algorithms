import bubble_sort
import unittest

class TestBubbleSort(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(bubble_sort.bubbleSort([5]), [5])
	
    def test_array(self):
        self.assertEqual(bubble_sort.bubbleSort([5,8,9,123,4]), [4,5,8,9,123])
	
    def test_negative_elements(self):
        self.assertEqual(bubble_sort.bubbleSort([3,9,-5,7,-10,11]), [-10,-5,3,7,9,11])
	
    def test_zero_element_array(self):
        self.assertEqual(bubble_sort.bubbleSort([1,3,2,0,-2]), [-2,0,1,2,3])

if __name__ == "__main__":
    unittest.main()
