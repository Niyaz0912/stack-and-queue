import unittest
from _01_Stack.Stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_0_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node.data, 5)


class TestStack(unittest.TestCase):
    stack = Stack()

    def test_1_init(self):
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.top, None)

    def test_2_push(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.top.data, 'test_data')
        self.stack.pop()

    def test_3_pop(self):
        self.stack.push('test_data')
        self.assertEqual(self.stack.pop(), 'test_data')
        self.assertEqual(self.stack.top, None)

    def test_4_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_5_is_full(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_6_clear_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.clear_stack()
        self.assertTrue(stack.is_empty())

    def test_7_get_data(self):
        stack = Stack()
        stack.push(1)
        stack.push("sta")
        stack.push(2)
        self.assertEqual(stack.get_data(1), "sta")
        self.assertEqual(stack.get_data(3), "Out of range")

    def test_8_size_stack(self):
        self.assertEqual(self.stack.stack_size, 5)

    def test_9_counter_int(self):
        stack = Stack()
        stack.push(1)
        stack.push("test")
        stack.push(2)
        stack.push(2.5)
        stack.push("string")
        self.assertEqual(stack.counter_int(), 2)
