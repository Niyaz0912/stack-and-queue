class Node:
    """Класс, представляющий узел в очереди. Здесь data: данные, хранящиеся в узле,
        next_node: ссылка на следующий узел в очереди."""
    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node


class Queue:
    """Класс, представляющий структуру данных очередь.Здесь head: начало очереди,
    tail: конец очереди."""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Функция для добавления элемента в очередь, data: данные для добавления в очередь."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        """Функция для извлечения элемента из очереди. Возвращает извлеченные данные из начала очереди."""
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data
