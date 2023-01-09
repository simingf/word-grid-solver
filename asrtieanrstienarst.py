def print_nums(path):
    print("+---+---+---+---+")
    for i in range(4):
        pos = [0,0,0,0]
        for j in range(4):
            for item in path:
                if (i,j) in path:
                    pos[j] = path.index((i,j))
            print('|' + pos[0] + '|' + pos[1] + '|' + pos[2] + '|')
            print("+---+---+---+---")
