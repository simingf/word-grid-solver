from trie import *

#config
num_rows = 4
num_cols = 4
multiple_paths_allowed = False

#global vars
game = []
answers = []
paths = []

def make_game():
    global game 
    rows = 0
    i = None
    while rows < num_rows:
        i = input()
        if len(i) != num_cols:
            print("Invalid input, try again")
            continue
        else:
            rows += 1
            game.append(list(i))    

def solve(root):
    for i in range(4):
        for j in range(4):
            visited = []
            visited.append((i, j))
            current_node = get_child(root, game[i][j])
            solve_recurse(current_node, i, j, game[i][j], visited)
    
def solve_recurse(node, x, y, word, visited):
    if is_endword(node) and (multiple_paths_allowed or word not in answers):
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

def sort_answers():
    global answers, paths
    answers, paths = zip(*sorted(zip(answers, paths), key=lambda x: len(x[0]), reverse=True))

def print_answers():
    print("Press enter for next answer")
    for i in range(len(answers)):
        input()
        print(answers[i])
        print_path(paths[i])

def print_path(path):
    print("+---+---+---+---+ +---+---+---+---+")
    for i in range(4):
        pos = [' ', ' ', ' ', ' ']
        for j in range(4):
            if (i, j) in path:
                pos[j] = str(path.index((i,j)) + 1)
                print("| " + game[i][j] + " ", end="")
            else:
                print("|   ", end="")
        print("|", end=" ")
        print("| " + pos[0] + " | " + pos[1] + " | " + pos[2] + " | " + pos[3] + " |")
        print("+---+---+---+---+ +---+---+---+---+")

if __name__ == "__main__":
    root = TrieNode()
    make_tree(root)
    make_game()
    solve(root)
    sort_answers()
    print_answers()