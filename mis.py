def maximum_independent_set(points, connections):
    """
    points: dict[int, (x, y)]
    connections: list[(int, int)]
    Rückgabe: set[int]  (IDs des MIS)
    """

    # Adjazenzliste
    adj = {v: set() for v in points}
    for u, v in connections:
        adj[u].add(v)
        adj[v].add(u)

    nodes = list(points.keys())
    best_set = set()

    def backtrack(current_set, remaining):
        nonlocal best_set

        # Pruning
        if len(current_set) + len(remaining) <= len(best_set):
            return

        if not remaining:
            if len(current_set) > len(best_set):
                best_set = current_set.copy()
            return

        v = remaining[0]

        # Fall 1: v nehmen
        new_remaining = [
            u for u in remaining[1:]
            if u not in adj[v]
        ]
        backtrack(current_set | {v}, new_remaining)

        # Fall 2: v nicht nehmen
        backtrack(current_set, remaining[1:])

    backtrack(set(), nodes)
    return best_set