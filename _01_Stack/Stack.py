class Node:
    """Класс для создания вершины стэка"""

    def __init__(self, data, next_node=None):
        """Функция инициализирует вершину стека. В data передаем данные, а next_node дает ссылку на следующую вершину
    (по умолчанию None)"""

        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для реализации стека"""

    def __init__(self, stack_size=5, top=None):
        """Функция инициализирует стек. Размер стека (максимум 5) и вершина стека (по умолчанию None)"""
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Функция добавляет данные в стек. Если стек переполнен, возвращает соответствующее сообщение"""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        """Функция удаляет последние добавленные данные. Если стек пуст, возвращает соответствующее сообщение"""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        """Функция проверяет, является ли стек пустым. Возвращает True если пуст, иначе False"""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Функция проверяет, является ли стек полным. Возвращает True если полон, иначе False"""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Функция через цикл wile полностью удаляет данные из стека"""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Функция используя цикл wile возвращает данные из стека по его индексу. Если указанный индекс находится
        вне диапозона возвращает сообение 'Out of range"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Функция через счетчик и цикл wile определяет размер стека. Возвращает количество элементов стека"""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Функция через счетчик и цикл wile определяет количество элементов int. Возвращает их количество"""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


stack = Stack()
stack.push(1)
stack.push("sta")
stack.push(2)
stack.push(2.5)
stack.push("sta")
print(stack.counter_int())

