from grid_creation import generate_grid, plot_graph
from mis import maximum_independent_set


def main():
    # -----------------------------
    # Parameter
    # -----------------------------
    GRID_SIZE = 15
    NUM_POINTS = 5
    MAX_CONNECTIONS = 18

    # -----------------------------
    # Grid erzeugen (ohne Plot)
    # -----------------------------
    points, connections = generate_grid(
        GRID_SIZE=GRID_SIZE,
        NUM_POINTS=NUM_POINTS,
        MAX_CONNECTIONS=MAX_CONNECTIONS,
    )

    # -----------------------------
    # Maximum Independent Set
    # -----------------------------
    mis = maximum_independent_set(points, connections)

    print("Maximum Independent Set:")
    print(sorted(mis))
    print("Größe:", len(mis))
    sol_str = ",".join(map(str,sorted(mis)))
    # -----------------------------
    # Graph plotten
    # -----------------------------
    plot_graph(points, connections, sol_str, GRID_SIZE, highlight_nodes=mis)


if __name__ == "__main__":
    main()