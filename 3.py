# Author: Kali Regenold

def fun1(tree_grid):
    tree_cnt = 0
    col = 0
    col_len = len(tree_grid[0])

    for row in tree_grid:
        # If tree_grid[row][col] == #, increase tree count
        tree_cnt += (row[col] == '#')
        # Increase column, but wrap to column length since the grid repeats to the right
        col = (col+3)%col_len

    print(tree_cnt)


def fun2(tree_grid):
    # Keep track of the tree count for each slope variation
    tree_cnt = [0]*5
    # Keep track of the column index for each slope variation
    col = [0]*5
    col_len = len(tree_grid[0])

    for row_idx, row_data in enumerate(tree_grid):
        for i in range(0,4):
            tree_cnt[i] += (row_data[col[i]] == '#')
            # First four slope variations increase column by 2
            col[i] = (col[i]+(i*2+1))%col_len
        if row_idx%2 == 0 and row_data[col[4]] == '#':
            tree_cnt[4] += 1
        # Last slope variation increases column by 1 on every other row
        col[4] = (col[4]+(1*(row_idx%2)))%col_len

    # Multiply tree counts together
    for i in range(1, 5):
        tree_cnt[0] *= tree_cnt[i]
    print(tree_cnt[0])


if __name__ == "__main__":
    # Read tree grid into a list separated by newline
    with open('3.in', 'r') as f:
        tree_grid = f.readlines()
    tree_grid = [x.strip() for x in tree_grid]
    fun1(tree_grid)
    fun2(tree_grid)
