package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type Student struct {
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Score int    `json:"score"`
}

// 匿名字段
type Train struct {
	Student
	int
	start time.Time
}

func main() {
	var stu Student = Student{
		Name:  "stu01",
		Age:   18,
		Score: 80,
	}

	data, err := json.Marshal(stu)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(data))

	// 访问结构体匿名字段
	var t Train
	t.int = 200
	t.Student.Name = "abc"
	t.Student.Age = 19
	// 也可以写成
	// t.Name = "abc"
	// t.Age = 19

	fmt.Println(t)

}
