def maximum_independent_set(points, connections):
    # -----------------------------
    # Build adjacency list
    # -----------------------------
    print(points, connections)
    print("MIS wird gestartet")
    
    adj = {v: set() for v in points}
    for u, v in connections:
        adj[u].add(v)
        adj[v].add(u)

    best = set()

    def branch(current_set, candidates):
        nonlocal best
        print(current_set,candidates)
        # ---- Branch & Bound ----
        if len(current_set) + len(candidates) <= len(best):
            return

        # ---- Leaf ----
        if not candidates:
            if len(current_set) > len(best):
                best = current_set.copy()
            return

        # Choose a branching vertex
        v = next(iter(candidates))

        # -----------------------------
        # Branch 1: INCLUDE v
        # Remove v and its neighbors
        # -----------------------------
        new_candidates = candidates - {v} - adj[v]
        branch(current_set | {v}, new_candidates)

        # -----------------------------
        # Branch 2: EXCLUDE v
        # Remove only v
        # -----------------------------
        branch(current_set, candidates - {v})

    branch(set(), set(points.keys()))
    return best