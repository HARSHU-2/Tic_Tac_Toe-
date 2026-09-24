b = [" "] * 9

for i in range(9):
    print(b[0], "|", b[1], "|", b[2])
    print("--+---+--")
    print(b[3], "|", b[4], "|", b[5])
    print("--+---+--")
    print(b[6], "|", b[7], "|", b[8])

    p = int(input("Enter position (1-9): ")) - 1
    b[p] = "X" if i % 2 == 0 else "O"

    for x, y, z in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[x] == b[y] == b[z] != " ":
            print(b[x], "wins!")
            exit()

print("Draw!")
