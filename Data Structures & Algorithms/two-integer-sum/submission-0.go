func twoSum(nums []int, target int) []int {
  hash := make(map[int]int)

  for i := range nums {
    if j, ok := hash[target-nums[i]]; ok {
      return []int{j, i}
    }
    hash[nums[i]] = i
  }

  return []int{}
}
