# link: https://leetcode-cn.com/problems/implement-trie-prefix-tree/


class TrieNodeDict:
    def __init__(self, val="/"):
        self.val = val
        self.children = {}
        self.is_end = False


class TrieDict:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNodeDict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                new_node = TrieNodeDict(c)
                root.children[c] = new_node
            root = root.children[c]
        root.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class TrieNode:
    def __init__(self, val="/"):
        self.val = val
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not root.children[idx]:
                new_node = TrieNode(c)
                root.children[idx] = new_node
            root = root.children[idx]
        root.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not root.children[idx]:
                return False
            root = root.children[idx]
        return root.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not root.children[idx]:
                return False
            root = root.children[idx]
        return True


if __name__ == "__main__":
    trie = TrieDict()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)