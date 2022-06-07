""" 208. Implement Trie (Prefix Tree) (Medium)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

!Note:
!You may assume that all inputs are consist of lowercase letters a-z.
!All inputs are guaranteed to be non-empty strings.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self._getNode()

    def _getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def _searchPrefix(self, prefix: str) -> TrieNode:
        node = self.root

        for level in range(len(word)):
            index = self._charToIndex(word[level])
            if not node.children[index]:
                return None

            node = node.children[index]

        return node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for level in range(len(word)):
            index = self._charToIndex(word[level])

            if not node.children[index]:
                node.children[index] = self._getNode()

            node = node.children[index]

        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._searchPrefix(word)

        return node != None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._searchPrefix(prefix)

        return node != None


if __name__ == "__main__":
    word = "a"
    prefix = "app"

    obj = Trie()
    # obj.insert(word)
    param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)

    print("Search result is {}".format(param_2))
    # print("StartsWith result is {}".format(param_3))
