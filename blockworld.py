def is_goal_state(state, goal_state):
    return state == goal_state

def apply_action(state, action):
    new_state = state[:]
    if action[0] == "Unstack":
        X, Y = action[1], action[2]
        new_state.remove((X, Y))
        new_state.append((X, "table"))
    elif action[0] == "Stack":
        X, Y = action[1], action[2]
        new_state.remove((X, "table"))
        new_state.append((X, Y))
    return new_state

def dfs(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, actions = stack.pop()

        if is_goal_state(current_state, goal_state):
            return actions

        for X, Y in current_state:
            if Y != "table":  # Unstack action: X is on top of Y
                new_action = ("Unstack", X, Y)
                new_actions = actions + [new_action]
                new_state = apply_action(current_state, new_action)
                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    stack.append((new_state, new_actions))

        # Only attempt to stack if the block is on the table
        for X, Y in current_state:
            if Y == "table":  # Only stack on top of another block (Z) or the table
                for Z in current_state:
                    if Z[1] != "table" and Z[0] != X:  # Z should not be "table" or the same block as X
                        new_action = ("Stack", X, Z[0])
                        new_actions = actions + [new_action]
                        new_state = apply_action(current_state, new_action)
                        if tuple(new_state) not in visited:
                            visited.add(tuple(new_state))
                            stack.append((new_state, new_actions))

    return None  # No solution found

# Example initial state and goal state
initial_state = [("A", "table"), ("B", "A"), ("C", "table")]
goal_state = [("A", "table"), ("B", "table"), ("C", "A")]

solution = dfs(initial_state, goal_state)

if solution:
    print("Solution Found!")
    for action in solution:
        print(f"{action[0]} {action[1]} {action[2]}")
else:
    print("No solution found.")
