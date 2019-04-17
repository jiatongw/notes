package main

import "fmt"

type Student struct {
	Name  string
	Age   int
	Score int
}

type Test interface {
	Print()
}

func (p Student) Print() {
	fmt.Println("name", p.Name)
	fmt.Println("age", p.Age)
	fmt.Println("score", p.Score)
}

func main() {
	var t Test
	var stu Student = Student{
		Name:  "stu1",
		Age:   19,
		Score: 100,
	}
	t = stu
	t.Print()
}
