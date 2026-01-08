from grid_creation import generate_grid
from mis import maximum_independent_set


def main():
    # -----------------------------
    # Parameter
    # -----------------------------
    GRID_SIZE = 15
    NUM_POINTS = 12
    MAX_CONNECTIONS = 18

    # -----------------------------
    # Grid erzeugen (ohne Plot)
    # -----------------------------
    points, connections = generate_grid(
        GRID_SIZE=GRID_SIZE,
        NUM_POINTS=NUM_POINTS,
        MAX_CONNECTIONS=MAX_CONNECTIONS,
        show_plot=False
    )

    # -----------------------------
    # Maximum Independent Set
    # -----------------------------
    mis = maximum_independent_set(points, connections)

    print("Maximum Independent Set:")
    print(sorted(mis))
    print("Größe:", len(mis))

    # -----------------------------
    # Grid erneut plotten + MIS hervorheben
    # -----------------------------
    generate_grid(
        GRID_SIZE=GRID_SIZE,
        NUM_POINTS=NUM_POINTS,
        MAX_CONNECTIONS=MAX_CONNECTIONS,
        show_plot=True,
        highlight_nodes=mis
    )


if __name__ == "__main__":
    main()