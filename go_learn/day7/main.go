package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	// os.Stdin 实现了 io.Reader 方法

	// 从终端读数据
	// reader := bufio.NewReader(os.Stdin)
	// str, err := reader.ReadString('\n') //readstring 的参数是byte, go里面byte是单引号
	// if err != nil {
	// 	fmt.Println("read string failed, err:", err)
	// }

	// fmt.Printf("read str success, ret:%s\n", str)

	// 从文件读数据

	// type CharCount struct {
	// 	CharCnt  int
	// 	NumCnt   int
	// 	SpaceCnt int
	// 	OtherCnt int
	// }

	// var count CharCount
	// file, err := os.Open("test.log")
	// if err != nil {
	// 	fmt.Println("read file err:", err)
	// 	return
	// }
	// defer file.Close()
	// reader := bufio.NewReader(file)
	// for {
	// 	str, err := reader.ReadString('\n') //readstring 的参数是byte, go里面byte是单引号
	// 	// EOF 表示读完了
	// 	if err == io.EOF {
	// 		break
	// 	}
	// 	if err != nil {
	// 		fmt.Println("read string failed, err:", err)
	// 		break
	// 	}

	// 	runeArr := []rune(str)
	// 	for _, v := range runeArr {
	// 		switch {
	// 		case v >= 'a' && v <= 'z':
	// 			fallthrough
	// 		case v >= 'A' && v <= 'Z':
	// 			count.CharCnt++
	// 		case v == ' ' || v == '\t':
	// 			count.SpaceCnt++
	// 		case v >= '0' && v <= '9':
	// 			count.NumCnt++
	// 		default:
	// 			count.OtherCnt++

	// 		}
	// 	}
	// }
	// fmt.Println(count)

	//JSON序列化城结构体

	// 如果要JSON序列化，需要大写，因为json是external的包
	// 也可以给每个字段加tag, 这样的话，json序列出来后，显示的字段就是tag
	type User struct {
		UserName string `json:"username"`
		NickName string
		Age      int
		Birthday string
		Sex      string
		Email    string
		Phone    string
	}

	user1 := &User{
		UserName: "user1",
		NickName: "user1",
		Age:      18,
		Birthday: "1998/1/1",
		Sex:      "Male",
		Email:    "123456@qq.com",
		Phone:    "138000000",
	}

	data, err := json.Marshal(user1)
	if err != nil {
		fmt.Println("json.marshal failed, err:", err)
		return
	}

	fmt.Printf("%s\n", string(data))

}
