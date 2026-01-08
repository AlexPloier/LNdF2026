import random
import matplotlib.pyplot as plt

# -----------------------------
# Hilfsfunktionen (intern)
# -----------------------------
def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def lines_intersect(A, B, C, D):
    # echte Linienkreuzung (gemeinsame Endpunkte erlaubt)
    if A in (C, D) or B in (C, D):
        return False
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

# -----------------------------
# Hauptfunktion
# -----------------------------
def generate_grid(
    GRID_SIZE: int,
    NUM_POINTS: int,
    MAX_CONNECTIONS: int,
    show_plot: bool = True
):
    """
    Erzeugt ein 2D-Grid mit zufälligen Punkten und kreuzungsfreien Verbindungen.

    Rückgabe:
        points: List[(x, y)]
        connections: List[((x1, y1), (x2, y2))]
    """

    # -----------------------------
    # Punkte erzeugen + nummerieren
    # -----------------------------
    raw_points = set()
    while len(raw_points) < NUM_POINTS:
        raw_points.add((
            random.randint(1, GRID_SIZE-1),
            random.randint(1, GRID_SIZE-1)
        ))

    points = {i: p for i, p in enumerate(raw_points)}

     # -----------------------------
    # Basis: jeder Punkt bekommt mind. 1 Verbindung
    # -----------------------------
    connections = []
    degrees = {pid: 0 for pid in points}

    ids = list(points.keys())
    random.shuffle(ids)

    for pid in ids:
        if degrees[pid] > 0:
            continue

        candidates = [other for other in ids if other != pid]

        random.shuffle(candidates)

        for other in candidates:
            if degrees[other] == 0 or True:
                p1, p2 = points[pid], points[other]

                for c1, c2 in connections:
                    if lines_intersect(p1, p2, points[c1], points[c2]):
                        break
                else:
                    connections.append((pid, other))
                    degrees[pid] += 1
                    degrees[other] += 1
                    break

    # -----------------------------
    # Zusätzliche Verbindungen (optional)
    # -----------------------------
    all_pairs = [
        (i, j)
        for i in ids
        for j in ids
        if i < j and (i, j) not in connections and (j, i) not in connections
    ]
    random.shuffle(all_pairs)

    for id1, id2 in all_pairs:
        if len(connections) >= MAX_CONNECTIONS:
            break

        p1, p2 = points[id1], points[id2]

        for c1, c2 in connections:
            if lines_intersect(p1, p2, points[c1], points[c2]):
                break
        else:
            connections.append((id1, id2))
            degrees[id1] += 1
            degrees[id2] += 1

    # -----------------------------
    # Plot
    # -----------------------------
    if show_plot:
        plt.figure(figsize=(6, 6))
        plt.xticks(range(GRID_SIZE + 1))
        plt.yticks(range(GRID_SIZE + 1))
        plt.grid(True)

        for pid, (x, y) in points.items():
            plt.scatter(x, y, s=100, zorder=3)
            plt.text(x + 0.1, y + 0.1,
                      str(pid), 
                      fontsize=14, 
                      fontweight="bold", 
                      color="black", 
                      zorder=4, 
                      bbox=dict(facecolor="white", edgecolor="none", alpha=0.7)
                    )

        for id1, id2 in connections:
            x1, y1 = points[id1]
            x2, y2 = points[id2]
            plt.plot([x1, x2], [y1, y2], zorder=2)

        plt.xlim(0, GRID_SIZE)
        plt.ylim(0, GRID_SIZE)
        plt.title("2D Grid: Finde das Maximal Independent Set")
        plt.show()

    return points, connections