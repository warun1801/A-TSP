import random

def fully_connected_graph_generator_to_csv(n, r):
    with open(f"fcgraph{n}.csv", "w") as f:
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i == n-1 and j == n:
                    f.write(str(i) + "," + str(j) + "," + str(random.randint(r[0], r[1])))
                # if i == j-1:
                    # f.write(str(i) + "," + str(j) + "," + str(1) + "\n")
                else:
                    f.write(str(i) + "," + str(j) + "," + str(random.randint(r[0], r[1])) + "\n")


def main():
    n = int(input("Enter number of nodes: "))
    r = [int(x) for x in input("Enter range of edge weights: ").split()]
    fully_connected_graph_generator_to_csv(n, r)

if __name__ == "__main__":
    main()