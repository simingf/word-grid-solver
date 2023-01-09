class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.endWord = False

    def insert(root, key):
        current_node = root
        for char in key:
            if current_node.children[ord(char) - ord('a')] == None:
                new_node = TrieNode()
                current_node.children[ord(char)] = new_node
            current_node = current_node.children[ord(char)]
        current_node.endWord = True
