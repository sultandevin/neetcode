class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const seen = {}

        // return early if strings dont have the same length
        if (s.length !== t.length) return false

        for (const ch of s) {
            seen[ch] = (seen[ch] || 0) + 1
        }
        for (const ch of t) {
            // if we havent seen this string return false
            if (!seen[ch]) return false
            seen[ch]--
        }

        return true
    }
}
