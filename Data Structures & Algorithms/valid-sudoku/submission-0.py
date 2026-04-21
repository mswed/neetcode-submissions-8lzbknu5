from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a dictionary containing a set for each row, column and box
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        # Iterate over all rows
        for r in range(9):
            # And over all columns
            for c in range(9):
                # We skip empty cells so we won't consider them as duplicates
                if board[r][c] != ".":
                    # The tricky part is finding the id for the column
                    box_id = (r // 3) * 3 + c // 3
                    # Check for duplicates
                    if (
                        board[r][c] in rows[r]
                        or board[r][c] in columns[c]
                        or board[r][c] in boxes[box_id]
                    ):
                        return False

                    # Add the value the row
                    rows[r].add(board[r][c])
                    # Add the value to the column
                    columns[c].add(board[r][c])
                    # Add the value to the box
                    boxes[box_id].add(board[r][c])

        return True
