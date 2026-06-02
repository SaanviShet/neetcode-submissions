class Solution:
    def check(self, line):
        isValid = [1]* 10
        for i in range(0, len(line)):
            if(line[i] != "."):
                isValid[int(line[i])] -= 1
                if(isValid[int(line[i])] < 0):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            if(not self.check(board[i][:])):
                return False
        
        for i in range(0, 9):
            column = [board[row][i] for row in range(9)]
            if(not self.check(column)):
                return False
        
        # [[0, 0][0, 1][0, 2]] ,[[1, 0][1, 1][1, 2]], [[2, 0][2, 1][2, 2]]

        res = [[["."] * 9 for _ in range(3)] for _ in range(3)]
        # print(res)
        # 0, 0 -> 0 ....0, 1 -> 1....0, 2 -> 2....1, 0 --> 3....1, 1 -> 4
        #  3 * (row % 3) + (col % 3)
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if(board[row][col] != "."):
                    res[row//3][col//3][3*(row % 3)+(col % 3)] = board[row][col]
        
        for i in range(0, len(res)):
            for j in range(0, len(res[0])):
                if (not self.check(res[i][j])):
                    return False
        
        return True



