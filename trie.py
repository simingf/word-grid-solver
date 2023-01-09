class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.endWord = False

def insert(root, key):
    current_node = root
    for char in key:
        pos = ord(char) - ord('a')
        if current_node.children[pos] == None:
            new_node = TrieNode()
            current_node.children[pos] = new_node
        current_node = current_node.children[pos]
    current_node.endWord = True

""" Probably don't need this """
def get_node(root, key):
    current_node = root
    for char in key:
        pos = ord(char) - ord('a')
        if current_node.children[pos] == None:
            return None
        current_node = current_node.children[pos]
    return current_node

def get_child(node, char):
    pos = ord(char) - ord('a')
    return node.children[pos]

def is_endword(node):
    return node.endWord

def get_words():
    words = []
    with open("words.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words

def make_tree(root):
    dictionary = get_words()
    for word in dictionary:
        insert(root,word)

if __name__ == "__main__":
    root = TrieNode()
    make_tree(root)
    print(get_node(root, "hello"))
    print(get_node(root, "asdf"))