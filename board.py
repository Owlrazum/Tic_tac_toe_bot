board = [
    ['x', 'o', 'x'],
    ['_', '_', 'x'],
    ['x', 'o', 'x']
]

def is_x_win(board):
    for row in range(3):
        xs = 0
        for col in range(3):
            if board[row][col] == 'x':
                xs += 1
        if xs == 3:
            return True

    for col in range(3):
        xs = 0
        for row in range(3):        
            if board[row][2] != 'x':
                xs += 1
        if xs == 3:
            return True
    
    left = 0
    right = 0
    x = 2
    y = 0
    for i in range(3):
        if board[i][i] == 'x':
            left += 1
        if board[x][y] == 'x':
            right += 1
        x -= 1
        y += 1
    if left == 3 or right == 3:
        return True
    else:
        return False
