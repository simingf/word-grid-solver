from trie import *
import random
import string
import copy

game = [['r', 'q', 'u', 'i'],
        ['e', 'i', 'n', 'c'],
        ['e', 'd', 'b', 'l'],
        ['n', 't', 'm', 'k']]

answers = []
paths = []

def solve(root):
    for i in range(4):
        for j in range(4):
            visited = []
            visited.append((i, j))
            current_node = get_child(root, game[i][j])
            solve_recurse(current_node, i, j, game[i][j], visited)
    
def solve_recurse(node, x, y, word, visited):
    if is_endword(node) and 8 >= len(word) >= 3 :
        answers.append(word)
        paths.append(visited)

    neighbors = get_neighbors(x, y)
    for (i, j) in neighbors:
        if (i, j) in visited:
            continue
        child = get_child(node, game[i][j])
        if child != None:
            visited_copy = visited[:]
            visited_copy.append((i, j))
            new_word = word + game[i][j]
            solve_recurse(child, i, j, new_word, visited_copy)

def get_neighbors(x, y):
    neighbors = []
    for i in range(max(0, x-1), min(3, x+1) + 1):
        for j in range(max(0, y-1), min(3, y+1) + 1):
            if i == x and j == y:
                continue
            else:
                neighbors.append((i,j))
    return neighbors

"""
def make_grid():
    for i in range(4):
        for j in range(4):
            randomLetter = random.choice(string.ascii_letters)
            grid[i][j] = randomLetter
"""

def print_answers():
    for i in range(len(answers)):
        print(answers[i])
        print_char_path(paths[i])

def print_char_path(path):
    print("+---+---+---+---+")
    for i in range(4):
        for j in range(4):
            if (i, j) in path:
                print("| " + game[i][j] + " ", end="")
            else:
                print("|   ", end="")
        print("|")
        print("+---+---+---+---+")

if __name__ == "__main__":
    root = TrieNode()
    make_tree(root)
    solve(root)
    print_answers()