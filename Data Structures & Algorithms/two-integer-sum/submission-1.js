class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hash = {}

        for (const [i, num] of nums.entries()) {
            const difference = target - num
            
            if (hash[difference] !== undefined) return [hash[difference], i]
            hash[num] = i
        }

        return []
    }
}
