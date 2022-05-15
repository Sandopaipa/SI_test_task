class ListNode:
    def __init__(self, nodedata, rand=None):
        self.prev = None
        self.data = nodedata
        self.next = None
        self.rand = rand


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def count(self):
        counter = 0
        current_node = self.head
        while current_node is not None:
            counter += 1
            current_node = current_node.next
        return counter

    def serializer(self):
        #Разделитель между ListNode.data и ListNode.rand
        split_rand = ','
        #Разделитель между узлами
        split_node = '\n'
        with open('test.json', 'w') as fl:
            current_node = self.head
            while current_node is not None:
                fl.write(str(current_node.data))
                if current_node.rand is not None:
                    #Установка разделителей
                    fl.write(split_rand)
                    #Запись информации в файл
                    fl.write(str(current_node.rand))
                    fl.write(split_node)
                else:
                    fl.write(split_rand)
                    fl.write(split_node)
                current_node = current_node.next

    def deserializer(self):
        #Буфер для временного хранения ListNode.data и ListNode.rand
        buf = []
        file_eof = ''
        lst = DoubleLinkedList()
        with open('test.json', 'r') as fl:
            while True:
                file = fl.readline().rstrip('\n')
                if file == file_eof:
                    break
                else:
                    buf = file.split(',')
                    buf[1].split('\n')
                    #Обработка исключения, если вторая ячейка массива пустая
                    #В этом случае ListNode.rand = None
                    try:
                        buf[1]
                    except IndexError:
                        #Добавление считанного элемента в список
                        if self.head is None:
                            new_node = ListNode(buf[0])
                            self.head = new_node
                            self.tail = new_node
                        else:
                            new_node = ListNode(buf[0])
                            self.tail.next = new_node
                            self.tail = new_node
                        #Продолжение считывания
                        continue
                    if self.head is None:
                        new_node = ListNode(buf[0], buf[1])
                        self.head = new_node
                        self.tail = new_node
                    else:
                        new_node = ListNode(buf[0], buf[1])
                        self.tail.next = new_node
                        self.tail = new_node
        return lst
