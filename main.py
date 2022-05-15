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

    def insert_in_list(self, data, rand=None):
        if self.head is None:
            new_node = ListNode(data, rand)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(data, rand)
            self.tail.next = new_node
            self.tail = new_node

    def serializer(self):
        split_rand = ','
        split_node = '\n'
        with open('test.json', 'w') as fl:
            current_node = self.head
            while current_node is not None:
                fl.write(str(current_node.data))
                if current_node.rand is not None:
                    fl.write(split_rand)
                    fl.write(str(current_node.rand))
                    fl.write(split_node)
                else:
                    fl.write(split_rand)
                    fl.write(split_node)
                current_node = current_node.next

    def deserializer(self):
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
                    try:
                        buf[1]
                    except IndexError:
                        lst.insert_in_list(buf[0], None)
                        continue
                    lst.insert_in_list(buf[0], buf[1])
        return lst
