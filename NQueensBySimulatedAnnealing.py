import random
import math

def calculate_conflicts(state):
    conflicts = 0
    N = len(state)
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_random_neighbor(state):
    N = len(state)
    new_state = state.copy()
    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)
    new_state[col] = row
    return new_state

def print_board(state):
    N = len(state)
    board = [["." for _ in range(N)] for _ in range(N)]
    for col in range(N):
        board[state[col]][col] = "Q"
    for row in board:
        print(" ".join(row))
    print()

def simulated_annealing_nqueens(N=4, max_steps=1000, start_temp=100, cooling_rate=0.95):
    current_state = [random.randint(0, N - 1) for _ in range(N)]
    current_cost = calculate_conflicts(current_state)
    temperature = start_temp
    print_board(current_state)

    for step in range(max_steps):
        if current_cost == 0:
            return current_state
        neighbor = get_random_neighbor(current_state)
        neighbor_cost = calculate_conflicts(neighbor)
        delta = neighbor_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_state, current_cost = neighbor, neighbor_cost
            print_board(current_state)
        temperature *= cooling_rate
        if temperature <= 0.01:
            break
    return current_state

solution = simulated_annealing_nqueens(4)
print("Final Solution:", solution)
print("Conflicts:", calculate_conflicts(solution))
