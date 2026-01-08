import random
import matplotlib.pyplot as plt


# ============================================================
# Geometrie-Hilfsfunktionen
# ============================================================
def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def lines_intersect(A, B, C, D):
    # Gemeinsame Endpunkte erlauben
    if A in (C, D) or B in (C, D):
        return False
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def point_on_segment(P, A, B, eps=1e-6):
    """
    Prüft, ob Punkt P auf dem Liniensegment AB liegt
    """
    # Kreuzprodukt = 0 → kollinear
    cross = (P[1] - A[1]) * (B[0] - A[0]) - (P[0] - A[0]) * (B[1] - A[1])
    if abs(cross) > eps:
        return False

    # Skalarprodukt → zwischen A und B
    dot = (P[0] - A[0]) * (B[0] - A[0]) + (P[1] - A[1]) * (B[1] - A[1])
    if dot < 0:
        return False

    sq_len = (B[0] - A[0])**2 + (B[1] - A[1])**2
    if dot > sq_len:
        return False

    return True

def valid_connection(p1, p2, points, connections):
    # 1️⃣ Keine Kreuzung mit bestehenden Kanten
    for c1, c2 in connections:
        if lines_intersect(p1, p2, points[c1], points[c2]):
            return False

    # 2️⃣ Kein anderer Punkt darf auf der Strecke liegen
    for pid, p in points.items():
        if p == p1 or p == p2:
            continue
        if point_on_segment(p, p1, p2):
            return False

    return True

def generate_grid(GRID_SIZE, NUM_POINTS, CONNECTION_PROB):
    """
    Rückgabe:
        points: dict[int, (x, y)]
        connections: list[(int, int)]
    """

    # -----------------------------
    # Punkte erzeugen + nummerieren
    # -----------------------------
    raw_points = set()
    while len(raw_points) < NUM_POINTS:
        raw_points.add((
            random.randint(1, GRID_SIZE - 1),
            random.randint(1, GRID_SIZE - 1)
        ))

    points = {i: p for i, p in enumerate(raw_points)}

    # -----------------------------
    # Basis: jeder Punkt mind. 1 Verbindung
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
            p1, p2 = points[pid], points[other]

            if valid_connection(p1, p2, points, connections):
                connections.append((pid, other))
                degrees[pid] += 1
                degrees[other] += 1
                break

    # -----------------------------
    # Zusätzliche Verbindungen (mit Wahrscheinlichkeit)
    # -----------------------------
    all_pairs = [
        (i, j)
        for i in ids
        for j in ids
        if i < j and (i, j) not in connections and (j, i) not in connections
    ]
    random.shuffle(all_pairs)

    for id1, id2 in all_pairs:
        # Wahrscheinlichkeit statt Max-Limit
        if random.random() > CONNECTION_PROB:
            continue

        p1, p2 = points[id1], points[id2]

        for c1, c2 in connections:
            if lines_intersect(p1, p2, points[c1], points[c2]):
                break
        else:
            connections.append((id1, id2))
            degrees[id1] += 1
            degrees[id2] += 1

    return points, connections

# ============================================================
# 2️⃣ Graph plotten (NUR VISUALISIERUNG)
# ============================================================
def plot_graph(points, connections, sol, GRID_SIZE, highlight_nodes=None):
    """
    highlight_nodes: set[int] oder None
    """

    plt.figure(figsize=(15, 10))
    plt.xticks(range(GRID_SIZE + 1))
    plt.yticks(range(GRID_SIZE + 1))
    plt.grid(True)

    # Kanten
    for id1, id2 in connections:
        x1, y1 = points[id1]
        x2, y2 = points[id2]
        plt.plot([x1, x2], [y1, y2], zorder=2)

    # Knoten + Labels
    for pid, (x, y) in points.items():
        plt.scatter(x, y, s=100, zorder=3)
        plt.text(
            x + 0.15,
            y + 0.15,
            str(pid),
            fontsize=14,
            fontweight="bold",
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.7),
            zorder=4
        )

        # Highlight (z. B. MIS)
        if highlight_nodes and pid in highlight_nodes:
            plt.scatter(
                x, y,
                s=220,
                facecolors="none",
                edgecolors="green",
                linewidths=2,
                zorder=5
            )

    plt.xlim(0, GRID_SIZE)
    plt.ylim(0, GRID_SIZE)
    plt.title("Das Maximal Independet Set ist: ["+sol+"]")
    plt.axis("off")
    plt.show()