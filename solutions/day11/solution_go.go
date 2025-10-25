// Problem: 3186. Maximum Total Damage With Spell Casting
// Solution: Dynamic Programming + Binary Search
// Author: https://github.com/harshwardhan-singh-bais
// Language: Go (Golang)
package main

import (
	"fmt"
	"sort"
)

func search(nums []int, l, r, target int) int {
	for l <= r {
		mid := (l + r) / 2
		if nums[mid] < target {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return l
}

func maximumTotalDamage(power []int) int {
	count := make(map[int]int)
	for _, v := range power {
		count[v]++
	}

	nums := make([]int, 0, len(count))
	for k := range count {
		nums = append(nums, k)
	}
	sort.Ints(nums)

	n := len(nums)
	t := make([]int, n+1)
	result := 0

	for i := n - 1; i >= 0; i-- {
		skip := 0
		if i+1 < n {
			skip = t[i+1]
		}

		j := search(nums, i+1, n-1, nums[i]+3)

		take := nums[i] * count[nums[i]]
		if j < n {
			take += t[j]
		}

		if take > skip {
			t[i] = take
		} else {
			t[i] = skip
		}

		if t[i] > result {
			result = t[i]
		}
	}

	return result
}

// --- For local testing ---
func main() {
	power := []int{1, 1, 3, 4}
	fmt.Println(maximumTotalDamage(power)) // Output: 6
}
