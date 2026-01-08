from grid_creation import generate_grid

def main():
    GRID_SIZE = 24
    NUM_POINTS = 12
    MAX_CONNECTIONS = 18

    points, connections = generate_grid(
        GRID_SIZE,
        NUM_POINTS,
        MAX_CONNECTIONS
    )

    print("Punkte:", points)
    print("Verbindungen:", connections)

if __name__ == "__main__":
    main()