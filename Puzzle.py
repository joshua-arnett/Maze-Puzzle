import heapq


def solve_puzzle(Puzzle, Source, Destination):
    """
    :param Puzzle: A 2D array containing hyphens and '#'s
    :param Source: Starting (a,b) coordinate tile
    :param Destination: Destination (x,y) coordinate tile

    Returns a tuple containing the shortest path, as well as the directions, required to reach the destination tile.
    """
    # Make sure Puzzle is a 2D array
    if Puzzle is not list or Puzzle[0] is not list:
        return None

    # Make sure all rows are of the same length
    row_length = len(Puzzle[0])
    for row in Puzzle:
        if len(row) != row_length:
            return None

    # Make sure Source and Destination are tuples with two integers
    if not (Source is tuple or Destination is tuple or
            len(Source) == 2 or len(Destination) == 2 or
            all(isinstance(v, int) for v in Source) or all(isinstance(v, int) for v in Destination)):
        return None
    from_i, from_j = Source
    to_i, to_j = Destination

    # If source and destination are the same
    if Source == Destination:
        return [Source], ''
    # If either source or destination is a blocked tile
    if Puzzle[from_i][from_j] == '#' or Puzzle[to_i][to_j] == '#':
        return None

    pq = [(0, Source, [Source], '')]  # (current_path_length, current_position, path_so_far, path_directions)
    visited = set()
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    while pq:
        # Get row and column indices, as well as effort to traverse to current node
        cost, (current_row, current_col), path_so_far, path_directions = heapq.heappop(pq)

        # If we have already visited the current node, skip it
        if (current_row, current_col) in visited:
            continue

        # Mark the current cell as visited
        visited.add((current_row, current_col))

        # If we are at the bottom-right cell, return the minimum effort used to reach it
        if (current_row, current_col) == Destination:
            return path_so_far, path_directions

        # Explore neighbors
        for move, (dr, dc) in directions.items():
            nr, nc = current_row + dr, current_col + dc
            if 0 <= nr < len(Puzzle) and 0 <= nc < len(Puzzle[0]) and Puzzle[nr][nc] == '-' and (nr, nc) not in visited:
                new_path = path_so_far + [(nr, nc)]
                heapq.heappush(pq, (cost + 1, (nr, nc), new_path, path_directions + move))

    # If no path is found
    return None
