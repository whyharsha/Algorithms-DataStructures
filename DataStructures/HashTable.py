import hashlib

class node(object):
    """
    Implements a node in a singly-linked list.
    """

    def __init__(self):
        self.key = ""
        self.value = None
        self.next = None
    
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class linked_list(object):
    """
    Implements a singly-linked list of nodes.
    """

    def __init__(self, head: node):
        self.head = head
    
    def insert(self, new_node: node):
        """
        Inserts a node into the singly-linked list.
        """
        if self.head is None:
            head = new_node
        else:
            last_node = self.head

            while last_node.next is not None:
                last_node = last_node.next
            
            last_node.next = new_node
    
    def remove(self, key: str):
        """
        Removes a node with the given key, if it exists.
        Returns the value at the node, if a node with the key exists.
        """

        if self.head is None:
            return None
        
        if self.head.key == key:
            tbd_node = self.head
            self.head = self.head.next
            return tbd_node.value
        
        if self.head.next is not None:
            tbd_node = self.head.next
            previous_node = self.head

            while tbd_node.next is not None:
                if tbd_node.key == key:
                    previous_node.next = tbd_node.next
                    return tbd_node.value
                else:
                    previous_node = tbd_node
                    tbd_node = tbd_node.next

                    if tbd_node.next is None:
                        if tbd_node.key == key:
                            previous_node.next = None
                            return tbd_node.value
        
        return None
    
    def get(self, key):
        """
        Returns the node with the given key and True.
        Returns last node if no such node exists and False.
        """

        if self.head is None:
            return (self.head, False)
        
        if self.head.key == key:
            return (self.head, True)
        
        if self.head.next is not None:
            current_node = self.head.next

            while current_node.next is not None:
                if current_node.key == key:
                    return (current_node, True)
                else:
                    current_node = current_node.next

                    if current_node.next is None:
                        return (current_node, False)
        else:
            return (self.head, False)

class hash_table:
    """
    Implements a hashtable with chaining.
    """
    def __init__(self):
        self.__min_size = 256
        self.__hash_map = [linked_list() for _ in range(0, self.__min_size)]
        self.__size = self.__min_size
        self.__count = 0
    
    def __hashing(self, input: str):
        k = 0
        
        for s in list(hashlib.sha256(input.encode('utf-8')).hexdigest()):
            k += ord(s)
        
        return k % len(self.__hash_map)
    
    def __setitem__(self, key: str, value):
        self.insert(key, value)
    
    def insert(self, key: str, value):
        """
        Inserts a value into the hash table with the given key.
        If the key already exists, replaces the existing value at the key.
        """
        self.__insert(key, value)

        if self.__count == self.__size:
            self.__grow_table()
    
    def __insert(self, key, value):
        hash_key = self.__hashing(key)
        bucket = self.__hash_map[hash_key]

        current_node, exists = bucket.get(hash_key)

        if current_node is not None:
            if exists:
                current_node.value = value
            else:
                current_node.next = node(hash_key, value, None)
        else:
            bucket.head = node(hash_key, value, None)
        
        self.__count += 1
    
    def __grow_table(self):
        """
        Doubles table size
        """

        self.__size = self.__size * 2

    def delete(self, key):
        """
        Deletes the value with the given key, if it exists.
        """

        if self.__count == (self.__size/2):
            self.__shrink_table()
    
    def __shrink_table(self):
        """
        Halves table size
        """

        self.__size = self.__size / 2