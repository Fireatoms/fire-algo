# link: https://leetcode-cn.com/problems/lru-cache/


class Node:
    def __init__(self, val=(-1, -1), next=None):
        self.val = val
        self.next = next


class LRUCache1:

    def __init__(self, capacity: int):
        self.count = 0
        self.capacity = capacity
        self.head = Node()

    def get(self, key: int) -> int:
        pre = self.head
        cur = self.head.next
        while cur:
            if cur.val[0] == key:
                pre.next = cur.next
                cur.next = self.head.next
                self.head.next = cur
                return cur.val[1]
            pre = pre.next
            cur = cur.next
        return -1

    def put(self, key: int, value: int) -> None:
        pre = self.head
        cur = self.head.next
        while cur:
            if cur.val[0] == key:
                cur.val = (key, value)
                break
            pre = pre.next
            cur = cur.next

        if cur:
            pre.next = cur.next
            cur.next = self.head.next
            self.head.next = cur
        else:
            if self.count >= self.capacity:
                pre = self.head
                cur = self.head.next
                while cur.next:
                    pre = pre.next
                    cur = cur.next
                pre.next = None
            else:
                self.count += 1

            new_node = Node((key, value))
            new_node.next = self.head.next
            self.head.next = new_node


# double linked list
class DoubleNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.dummy_head = DoubleNode()
        self.dummy_tail = DoubleNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_to_head(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.move_to_head(self.cache[key])
        else:
            new_node = DoubleNode(key, value)
            self.add_to_head(new_node)
            self.cache[key] = new_node
            self.count += 1
            if self.count > self.capacity:
                tail_node = self.remove_tail()
                self.cache.pop(tail_node.key)
                self.count -= 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.prev = self.dummy_head
        node.next = self.dummy_head.next
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        tail_node = self.dummy_tail.prev
        self.remove_node(tail_node)
        return tail_node

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    cache.put(1, 1)
    cache.get(2)
    cache.put(3, 3)
    print(cache.get(1))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)