from aula_03.node import Node
# sequencial = []
# sequencial.append(7)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista ja possuui elemento
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        """
        Retorna o tamanho da lista
        """
        return self._size

    def _getnode(self, index):
        pointer = self.head
        if pointer:
            pointer = pointer.next
        else:
            raise IndexError('List index out out range')
        return pointer

    def __getitem__(self, index):
        
        pointer = self._getnode()
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('List index out out range')
            if pointer:
                return pointer.data
            else:
                raise IndexError('List index out of range')

    def __setitem__(self, index, elem):

        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('List index out out range')
            if pointer:
                pointer.data = elem
            else:
                raise IndexError('List index out of range')

    def index(self, elem):
        """
        Retorna i indice do elem da lista
        """
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem):

        # inserir no inicio da lista
        if index == 0:
            node = Node(elem)
            # Node recem criado será o primeiro
            node.next = self.head
            self.head = node
        else:
            pointer = self.head
            for i in range(index):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError('List index out of range')



if __name__ == '__main__':
    # lista = []
    # lista.append(7)
    lista = LinkedList()
    lista.append(5)
    lista.append(8)
    lista.append(9)
    print(lista.index(9))





