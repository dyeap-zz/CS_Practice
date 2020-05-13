
# https://www.youtube.com/watch?v=hjUJFjcrbR4
class Trie:
    def __init__(self):
        self.root = {"*":"*"}
    def add_word(self,word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                # add letter to dictionary
                curr_node[letter] = {}
            # move pointer down
            curr_node = curr_node[letter]
        curr_node["*"] = "*"

    def does_word_exist(self,word):
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]
        return "*" in curr_node

trie = Trie()
trie.add_word("wait")
trie.add_word("waiter")
print(trie.does_word_exist(""))

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self,word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_end_word = True

    def does_word_exist(self,word):
        if word == "": return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_word


trie = Trie()
trie.add_word("wait")
print(trie.does_word_exist(""))

'''

