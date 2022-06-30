rows = int(input())
board = []

for _ in range(rows):
    board.append([x for x in input().split()])

# initialize 2D array for visited steps
visited_steps = [[False] * len(board[0]) for _ in range(len(board))]


def get_next_positions(pos):
    # calculate valid steps from current position pos
    # store them as tuples in next_step list. Return that list
    x, y = pos
    # directions we can move --> right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    next_steps = []
    for direction in directions:
        if ((x + direction[0]) < 0) or ((y + direction[1]) < 0) \
                or ((x + direction[0]) > len(board) - 1) \
                or ((y + direction[1]) > len(board[0]) - 1):
            continue
        next_steps.append((x + direction[0], y + direction[1]))
    return next_steps


def get_connections_count(stack):
    connections = 0
    while stack:
        # get the (x, y) coordinates of the top stack position
        x, y = stack.pop()

        # since (x, y) is a dot, we initialize the connections counter with that dot itself --> 1
        # every pair (x, y) in the stack implies a connection
        connections += 1

        # mark current (x, y) position as visited
        if not visited_steps[x][y]:
            visited_steps[x][y] = True

        next_steps = get_next_positions((x, y))

        for next_step in next_steps:
            next_x, next_y = next_step

            if board[next_x][next_y] == "-" \
                    or visited_steps[next_x][next_y]:
                continue

            stack.append((next_x, next_y))
            if not visited_steps[next_x][next_y]:
                visited_steps[next_x][next_y] = True

    return connections


all_connections = []
temp = []
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "." and not visited_steps[i][j]:
            visited_steps[i][j] = True
            temp.append((i, j))
            all_connections.append(get_connections_count(temp))
            temp.clear()

print(max(all_connections))