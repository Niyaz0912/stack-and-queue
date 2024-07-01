import unittest
from _02_Queue.Queue import Node, Queue


class TestQueueMethods(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.head.data, 1)

        queue.enqueue(2)
        self.assertEqual(queue.head.data, 1)  # Проверяем, что первый элемент остался неизменным
        self.assertEqual(queue.tail.data, 2)  # Проверяем, что второй элемент стал хвостом

    def test_dequeue(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())  # Проверяем dequeue при пустой очереди

        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)  # Проверяем извлечение первого элемента
        self.assertEqual(queue.dequeue(), 2)  # Проверяем извлечение второго элемента

        self.assertIsNone(queue.head)  # Проверяем, что голова пуста после извлечения всех элементов

    def test_queue_order(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)  # Проверяем порядок элементов при извлечении
        self.assertEqual(queue.dequeue(), 2)  # Проверяем порядок элементов при извлечении
        self.assertEqual(queue.dequeue(), 3)  # Проверяем порядок элементов при извлечении
        self.assertIsNone(queue.head)  # Проверяем, что голова пуста после извлечения всех элементов
