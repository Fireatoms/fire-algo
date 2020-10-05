# link: https://leetcode-cn.com/problems/lru-cache/


class DoubleNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.dummy_head = DoubleNode()
        self.dummy_tail = DoubleNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            new_node = DoubleNode(key, value)
            self.add_to_head(new_node)
            self.cache[key] = new_node
            self.count += 1
            if self.count > self.capacity:
                deleted_node = self.remove_tail()
                self.cache.pop(deleted_node.key)
                self.count -= 1

    def remove_tail(self):
        deleted_node = self.dummy_tail.pre
        self.remove(deleted_node)
        return deleted_node

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add_to_head(self, node):
        node.next = self.dummy_head.next
        node.pre = self.dummy_head
        self.dummy_head.next.pre = node
        self.dummy_head.next = node

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)