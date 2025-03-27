def compute_opt(weights, benefits, W, n):
    OPT = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    keep = [[False for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill the OPT and keep tables
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:  # Cannot include item i
                OPT[i][j] = OPT[i - 1][j]
                keep[i][j] = False
            else:
                # Decide whether to include item i
                if benefits[i - 1] + OPT[i - 1][j - weights[i - 1]] > OPT[i - 1][j]:
                    OPT[i][j] = benefits[i - 1] + OPT[i - 1][j - weights[i - 1]]
                    keep[i][j] = True
                else:
                    OPT[i][j] = OPT[i - 1][j]
                    keep[i][j] = False

    return OPT, keep


def print_table(OPT, n, W):
    print("OPT Table:")
    for i in range(n + 1):
        for j in range(W + 1):
            print(f"{OPT[i][j]:2}", end=" ")
        print()
def print_keep_table(keep, n, W):
    print("\nKeep Table (Selected Items):")
    for i in range(n + 1):
        for j in range(W + 1):
            print("T" if keep[i][j] else "F", end=" ")
        print()

if __name__ == '__main__':
    # Define the weights and benefits of each item
    weights = [4, 6, 5, 7, 3, 1, 6]  # Weights of items a, b, c, d, e, f, g
    benefits = [12, 10, 8, 11, 14, 7, 9]  # Benefits of items a, b, c, d, e, f, g
    W = 18  # Maximum weight capacity
    n = len(weights)  # Number of items

    # Compute OPT and keep tables
    OPT, keep = compute_opt(weights, benefits, W, n)

    # Print the OPT table
    print_table(OPT, n, W)
    print_keep_table(keep, n, W)



