from collections import deque

def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True

def is_goal(state):
    return state == (0, 0, 0, 3, 3)

def generate_next_states(state):
    m_left, c_left, boat, m_right, c_right = state
    next_states = []
    
    if boat == 1:  # Boat is on the left side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c)
            if is_valid(new_state):
                next_states.append(new_state)
    else:  # Boat is on the right side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c)
            if is_valid(new_state):
                next_states.append(new_state)
    
    return next_states

def solve():
    initial_state = (3, 3, 1, 0, 0)
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()
        if is_goal(current_state):
            return path + [current_state]
        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))
    return None

def print_solution(path):
    if path:
        for state in path:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    solution = solve()
    print_solution(solution)