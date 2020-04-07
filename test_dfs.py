import unittest
import DFS

test1 = DFS.Node("A")
test1.add_child("B").add_child("C")
test1.children[0].add_child("D")

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test1.depth_first_search([]), ["A", "B", "D", "C"])

if __name__ == "__main__":
    unittest.main()
