package main

import "fmt"

func main() {
	// fmt.Println("Bootajay")

	// var abc, def = false, 123

	// fmt.Println(abc)
	// fmt.Println(def)

	f := fibonacci()
	for i := 0; i < 15; i++ {
		fmt.Println(f())
	}
}

func fibonacci() func() int {
	first, second := 0, 1

	return func() int {
		ret := first
		first, second = second, first+second
		return ret
	}
}
