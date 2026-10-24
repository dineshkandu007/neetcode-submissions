class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
 isValidSudoku(board) {
  // Create 9 sets to track numbers seen in each row
  const rows = Array.from({ length: 9 }, () => new Set());

  // Create 9 sets to track numbers seen in each column
  const cols = Array.from({ length: 9 }, () => new Set());

  // Create 9 sets to track numbers seen in each 3×3 sub-box
  const boxes = Array.from({ length: 9 }, () => new Set());

  // Loop through each row (0 to 8)
  for (let r = 0; r < 9; r++) {

    // Loop through each column (0 to 8)
    for (let c = 0; c < 9; c++) {

      // Get the value at the current cell
      const val = board[r][c];

      // If the cell is empty, skip it
      if (val === '.') continue;

      // Calculate the index of the 3×3 box this cell belongs to
      // Rows 0–2 → top boxes, 3–5 → middle, 6–8 → bottom
      // Columns 0–2 → left boxes, 3–5 → middle, 6–8 → right
      const boxIndex = Math.floor(r / 3) * 3 + Math.floor(c / 3);

      // Check if the number already exists in:
      // 1) the current row
      // 2) the current column
      // 3) the current 3×3 box
      if (
        rows[r].has(val) ||
        cols[c].has(val) ||
        boxes[boxIndex].has(val)
      ) {
        // If any duplicate is found, Sudoku is invalid
        return false;
      }

      // Add the value to the corresponding row set
      rows[r].add(val);

      // Add the value to the corresponding column set
      cols[c].add(val);

      // Add the value to the corresponding 3×3 box set
      boxes[boxIndex].add(val);
    }
  }

  // If no duplicates were found, the Sudoku board is valid
  return true;
}

}
