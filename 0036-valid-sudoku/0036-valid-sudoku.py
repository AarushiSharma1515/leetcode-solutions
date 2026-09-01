class Solution(object):
    def isValidSudoku(self, board):
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                
                val=board[r][c]
                if val==".":
                    continue
                keys=(r//3,c//3)
                if val in rows[r] or val in cols[c] or val in boxes[keys]:
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[keys].add(val)
        return True
