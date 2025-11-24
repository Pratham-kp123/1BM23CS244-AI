import math

# Alpha-Beta Pruning
def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    # If leaf node
    if depth == 0 or isinstance(node, int):
        return node

    if maximizingPlayer:
        value = -math.inf
        for child in node:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                print(f"Pruned in MAX node: alpha={alpha}, beta={beta}")
                break
        return value

    else:  # Minimizing player
        value = math.inf
        for child in node:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Pruned in MIN node: alpha={alpha}, beta={beta}")
                break
        return value


# Example tree
game_tree = [
    [3, 5, 6],      # A
    [1, 2, 4],      # B
    [7, 9, 8]       # C
]

# Run Alpha-Beta
result = alphabeta(game_tree, 2, -math.inf, math.inf, True)
print("\nFinal Result (Best value for Max):", result)
