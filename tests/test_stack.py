import unittest
from src.stack import Node, Stack

class Test(unittest.TestCase):

    def test_Node_1(self):
        n1 = Node(1000, None)
        self.assertEqual(n1.data, 1000)

    def test_Node_2(self):
        n1 = Node(1, 1000)
        self.assertEqual(n1.next_node, 1000)

    def test_Node_3(self):
        stack = Stack()
        stack.push("datas")
        stack.push("datas_2")
        self.assertEqual(stack.top.data, "datas_2")

    def test_Node_4(self):
        stack = Stack()
        stack.push("datas")
        stack.push("datas_2")
        stack.pop()
        self.assertEqual(stack.top.data, "datas")

    def test_Node_5(self):
        stack = Stack()
        stack.push('data')
        self.assertEqual(str(stack), str(["data"]))