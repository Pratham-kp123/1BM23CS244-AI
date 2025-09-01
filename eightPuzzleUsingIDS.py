from copy import deepcopy

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def print_state(state):
    for row in state:
        print(row)
    print("-" * 10)

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, direction):
    x, y = find_zero(state)
    dx, dy = DIRECTIONS[direction]
    nx, ny = x + dx, y + dy

    if 0 <= nx < 3 and 0 <= ny < 3:
        new_state = deepcopy(state)
        new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
        return new_state
    return None

def DLS(current_state, goal_state, depth_limit, path, visited):
    print_state(current_state)

    if current_state == goal_state:
        return path + [current_state]

    if depth_limit == 0:
        return None

    visited.add(state_to_tuple(current_state))

    for direction in ['up', 'down', 'left', 'right']:
        new_state = move(current_state, direction)
        if new_state:
            new_state_key = state_to_tuple(new_state)
            if new_state_key not in visited:
                result = DLS(new_state, goal_state, depth_limit - 1, path + [current_state], visited)
                if result:
                    return result

    return None

def IDS(start_state, goal_state):
    depth_limit = 0

    while True:
        visited = set()
        result = DLS(start_state, goal_state, depth_limit, [], visited)

        if result:
            return result

        depth_limit += 1

if __name__ == "__main__":
    print("Enter the initial 3x3 puzzle state (use 0 for the blank):")
    initial_state = []
    for i in range(3):
        row = input(f"Row {i+1} (space-separated): ").strip().split()
        initial_state.append([int(num) for num in row])

    solution_path = IDS(initial_state, GOAL_STATE)

    if solution_path:
        print("Solution Path (step-by-step):")
        for idx, state in enumerate(solution_path):
            print(f"Step {idx}:")
            print_state(state)
        print("Puzzle Solved!")
    else:
        print("No solution found.")
