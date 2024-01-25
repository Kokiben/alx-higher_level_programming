#!/usr/bin/python3

"""Class definition for a singly-linked list."""


class Node:
    """A simple represention of a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """nitialize a new Node with a specified data.

        Args:
            data (int): Data of new Node.
            next_node (Node): Next node of new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of Node."""
        return (self.__data)

    @data.setter
    def data(self, val):
        if not isinstance(val, int):
            raise TypeError("data must be an integer")
        self.__data = val

    @property
    def next_node(self):
        """Get next_node of Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, val):
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = val


class SinglyLinkedList:
    """"A simple represention a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList with a specified head."""
        self.__head = None

    def sorted_insert(self, val):
        """Add a fresh Node to the SinglyLinkedList.

        The node is added to the list in the appropriate
        numerical order.

        Args:
            val (Node): The new Node to add.
        """
        n = Node(val)
        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data > val:
            n.next_node = self.__head
            self.__head = n
        else:
            tp = self.__head
            while (tp.next_node is not None and
                    tp.next_node.data < val):
                tp = tp.next_node
            n.next_node = tp.next_node
            tp.next_node = n

    def __str__(self):
        """Specify the print() representation for SinglyLinkedList."""
        vals = []
        tp = self.__head
        while tp is not None:
            vals.append(str(tp.data))
            tp = tp.next_node
        return ('\n'.join(vals))
