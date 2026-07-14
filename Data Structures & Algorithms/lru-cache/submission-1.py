class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key -> Node
        
        # Initialize dummy head & tail to easily handle boundary conditions
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Helper to remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node) -> None:
        """Helper to insert a node right before the dummy tail (marking it MRU)."""
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Since it was accessed, move it to the tail (MRU)
        self._remove(node)
        self._add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, update its value and move to tail
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            # Create a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)
            
            # If capacity is exceeded, evict the LRU node (just after head)
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]  # Remove from map using key stored in node