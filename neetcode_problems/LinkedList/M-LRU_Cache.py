# Hint: use a doubly linked list to track order and a hashmap for easy lookup
# Only thing I forgot was when accessing the hashmap, order should also be upated.

class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # stack + hashmap?
        self.nums = 0
        self.cap = capacity
        self.hashing = {}

        self.list_start = Node(val=None)
        self.list_end = Node(val=None)
        self.list_start.next = self.list_end
        self.list_end.prev = self.list_start

    def get(self, key: int) -> int:
        if key in self.hashing:
            node = self.hashing[key]
            # move to front
            node.prev.next = node.next
            node.next.prev = node.prev
            
            s_old = self.list_start.next
            self.list_start.next = node
            node.prev = self.list_start
            node.next = s_old
            s_old.prev = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashing:
            # in cache so move existing to front
            self.hashing[key].val = value

            p = self.hashing[key].prev
            n = self.hashing[key].next
            p.next = n
            n.prev = p

            s_old = self.list_start.next
            self.list_start.next = self.hashing[key]
            self.hashing[key].prev = self.list_start
            self.hashing[key].next = s_old
            s_old.prev = self.hashing[key]
            return

        if self.nums >= self.cap:
            # remove end one for space
            node_to_del = self.list_end.prev
            end_new = node_to_del.prev
            del self.hashing[node_to_del.key]
            del node_to_del
            self.nums -= 1

            end_new.next = self.list_end
            self.list_end.prev = end_new
        
        # there is enough space, populate to the start
        s_old = self.list_start.next
        new = Node(key, value, next=s_old, prev=self.list_start)
        self.hashing[key] = new
        self.nums += 1

        self.list_start.next = new
        s_old.prev = new
