class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums
) {
  let result = [];
  for (let i = 0; i < 2; i++) {
   for (let j = 0; j < nums.length; j++) {
    result.push(nums[j]);
   }
  }
  return result;
  } 
}
