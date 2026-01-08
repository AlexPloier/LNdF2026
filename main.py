from grid_creation import generate_grid, plot_graph
from mis import maximum_independent_set


def main():
    # -----------------------------
    # Parameter
    # -----------------------------
    GRID_SIZE = 32
    NUM_POINTS = 54
    CONNECTION_PROB= 0.2

    # -----------------------------
    # Grid erzeugen (ohne Plot)
    # -----------------------------
    points, connections = generate_grid(
        GRID_SIZE=GRID_SIZE,
        NUM_POINTS=NUM_POINTS,
        CONNECTION_PROB=CONNECTION_PROB,
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