class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sHash = {}
        const tHash = {}

        const sArr = s.split("")
        const tArr = t.split("")

        sArr.forEach(el => {
            if (sHash[el]) {
                sHash[el]++
            } else {
                sHash[el] = 1
            }
        })

        tArr.forEach(el => {
            if (tHash[el]) {
                tHash[el]++
            } else {
                tHash[el] = 1
            }
        })

        let flag = true
        Object.keys(sHash).forEach(key => {
            if (sHash[key] !== tHash[key]) flag = false
        })

        Object.keys(tHash).forEach(key => {
            if (sHash[key] !== tHash[key]) flag = false
        })

        return flag
    }
}
