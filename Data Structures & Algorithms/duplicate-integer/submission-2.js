class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = {}
        
        for (let i = 0, length = nums.length; i < length; i++) {
            if (seen[nums[i]]) {
                return true    
            }
            seen[nums[i]] = true
        }

        return false
    }
}
