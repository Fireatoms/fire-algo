# link: https://leetcode-cn.com/problems/lru-cache/


class DubbleNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.dummy_head = DubbleNode()
        self.dummy_tail = DubbleNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_head(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # do not forget update val in self.cache
            self.cache[key].val = value
            self.move_to_head(self.cache[key])
        else:
            new_node = DubbleNode(key, value)
            self.add_to_head(new_node)
            self.cache[key] = new_node
            self.count += 1
            if self.count > self.capacity:
                deleted_node = self.remove_tail()
                self.cache.pop(deleted_node.key)

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.prev = self.dummy_head
        node.next = self.dummy_head.next
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

    def remove_tail(self):
        deleted_node = self.dummy_tail.prev
        self.remove(deleted_node)
        return deleted_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)