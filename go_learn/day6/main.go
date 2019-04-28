package main

import "fmt"

type Car interface {
	GetName() string
	Run()
	DiDi()
}

type BMW struct {
	Name string
}

func (b *BMW) GetName() string {
	return b.Name
}
func (b *BMW) Run() {
	fmt.Println("This is: ", b.Name)
}
func (b *BMW) DiDi() {
	fmt.Println("DiDi")
}

type BYD struct {
	Name string
}

func (b *BYD) GetName() string {
	return b.Name
}
func (b *BYD) Run() {
	fmt.Println("This is: ", b.Name)
}
func (b *BYD) DiDi() {
	fmt.Println("DiDi")
}
func main() {
	var car Car
	bmw := BMW{
		Name: "BMW",
	}
	byd := BYD{
		Name: "BYD",
	}
	car = &bmw
	car.Run()
	car = &byd
	car.Run()
}
