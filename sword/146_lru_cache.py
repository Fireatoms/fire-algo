# link: https://leetcode-cn.com/problems/lru-cache/

class DoubleNode:
    def __init__(self, key=0, val=0, next=None, pre=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.head = DoubleNode()
        self.cache = {}
        self.dummy_head = DoubleNode()
        self.dummy_tail = DoubleNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.val
        return -1

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        node.next = self.dummy_head.next
        node.pre = self.dummy_head
        self.dummy_head.next.pre = node
        self.dummy_head.next = node

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def remove_tail(self):
        last_node = self.dummy_tail.pre
        self.remove(last_node)
        return last_node

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
                remove_node = self.remove_tail()
                self.cache.pop(remove_node.key)
                self.count -= 1

    def print_lru(self):
        head = self.dummy_head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return "=>".join(map(str, res[1:-1]))


if __name__ == "__main__":
    lc = LRUCache(2)
    lc.put(1, 1)
    lc.put(2, 2)
    print(lc.get(1))
    lc.put(3, 3)
    print(lc.print_lru())