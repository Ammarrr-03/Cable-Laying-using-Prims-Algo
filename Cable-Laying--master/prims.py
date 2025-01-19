def calculate_mst(cost, n):
    visited = [0] * (n + 1)
    ne = 1
    mincost = 0
    a = b = u = v = 0

    visited[1] = 1

    print("\n")
    
    while ne < n:
        min_val = 999
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if cost[i][j] < min_val:
                    if visited[i] != 0:
                        min_val = cost[i][j]
                        a = u = i
                        b = v = j

        if visited[u] == 0 or visited[v] == 0:
            print(f"Connection {a}-{b} distance: {min_val}")
            ne += 1
            mincost += min_val
            visited[b] = 1

        cost[a][b] = cost[b][a] = 999

    return mincost

def main():
    n = int(input("Enter the number of companies: "))
    cost = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    print("\nEnter the distance between them:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost[i][j] = int(input())
            if cost[i][j] == 0:
                cost[i][j] = 999

    mincost = calculate_mst(cost, n)

    print("\nMinimum cost for laying a cable =", mincost)

if __name__ == "__main__":
    main()
