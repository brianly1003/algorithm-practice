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


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.root

        for ch in word:
            if ch not in trie:
                trie[ch] = {}

            trie = trie[ch]

        trie['*'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.root

        for ch in word:
            if ch not in trie:
                return False

            trie = trie[ch]

        return '*' in trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.root

        for ch in prefix:
            if ch not in trie:
                return False

            trie = trie[ch]

        return True


if __name__ == "__main__":
    word = "apple"
    prefix = "app"

    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)

    print("Search result is {}".format(param_2))
    print("StartsWith result is {}".format(param_3))
