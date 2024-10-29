store = []
for i in range(26):
    store.append({
    '1': 0,
    '3': 0,
    '2': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
})


board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

vertical = 0
horizontal = 9 
square = 18

for i in range(0, len(board)):
    for j in range(0, len(board)):

        if board[j][i] in store[vertical]:
            store[vertical][board[j][i]] += 1
            if store[vertical][board[j][i]] > 1:
                print("INVALID")

        if board[i][j] in store[horizontal]:
            store[horizontal][board[i][j]] += 1
            if store[horizontal][board[i][j]] > 1:
                print("INVALID")

    vertical += 1
    horizontal += 1 


y = 0

while y != 9:
    x = 0
    while x != 9:
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                print([i, j])
        print()
        x += 3
    y += 3
    print()
