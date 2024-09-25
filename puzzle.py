import itertools
import random
from collections import deque

class PuzzleState:
    def __init__(self, tiles, empty_tile_index, parent=None):
        self.tiles = tiles
        self.empty_tile_index = empty_tile_index
        self.parent = parent

    def __eq__(self, other):
        return self.tiles == other.tiles

    def __hash__(self):
        return hash(tuple(self.tiles))

    def is_goal(self):
        return self.tiles == list(range(1, 9)) + [0]

    def get_possible_moves(self):
        moves = []
        row, col = divmod(self.empty_tile_index, 3)

        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        for direction, (dr, dc) in directions.items():
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_empty_tile_index = new_row * 3 + new_col
                new_tiles = self.tiles[:]
                new_tiles[self.empty_tile_index], new_tiles[new_empty_tile_index] = new_tiles[new_empty_tile_index], new_tiles[self.empty_tile_index]
                moves.append(PuzzleState(new_tiles, new_empty_tile_index, self))
        return moves

def bfs(initial_state):
    if initial_state.is_goal():
        return initial_state

    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()
        for next_state in current_state.get_possible_moves():
            if next_state not in visited:
                if next_state.is_goal():
                    return next_state
                queue.append(next_state)
                visited.add(next_state)
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent

    path.reverse()
    for state in path:
        display_puzzle(state.tiles)
        print(" ")

def display_puzzle(tiles):
    for i in range(0, 9, 3):
        print(tiles[i:i + 3])

def create_initial_state():
    tiles = list(range(1, 9)) + [0]
    random.shuffle(tiles)
    while not is_solvable(tiles):
        random.shuffle(tiles)
    return PuzzleState(tiles, tiles.index(0))

def is_solvable(tiles):
    inversion_count = 0
    for i, j in itertools.combinations(range(len(tiles)), 2):
        if tiles[i] != 0 and tiles[j] != 0 and tiles[i] > tiles[j]:
            inversion_count += 1
    return inversion_count % 2 == 0

def main():
    initial_state = create_initial_state()
    print("Initial State:")
    display_puzzle(initial_state.tiles)
    print("")

    solution = bfs(initial_state)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()