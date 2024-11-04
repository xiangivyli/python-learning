class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialise sets for rows, columns and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num != ".":
                    box_index = (i // 3) * 3 + (j // 3)

                    if (num in rows[i]) or  (num in cols[j]) or (num in boxes[box_index]):
                        return False

                    # add the num to the set
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)

        return True 

# key1: using set for unique check
# key2: indexing to identify each num
# key3: box_index = (i // 3) * 3 + (j // 3)
# time complexity: O(1)
# space complexity: O(1)   
