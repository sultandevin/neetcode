func isAnagram(s string, t string) bool {
    	sHash := make(map[byte]int)
	tHash := make(map[byte]int)

	for i := range s {
		sHash[s[i]]++
	}
	for i := range t {
		tHash[t[i]]++
	}

	for char := range sHash{
		if sHash[char] != tHash[char] {
			return false
		}
	}

	for char := range tHash{
		if sHash[char] != tHash[char] {
			return false
		}
	}

	return true

}


