package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
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

	type CharCount struct {
		CharCnt  int
		NumCnt   int
		SpaceCnt int
		OtherCnt int
	}

	var count CharCount
	file, err := os.Open("test.log")
	if err != nil {
		fmt.Println("read file err:", err)
		return
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	for {
		str, err := reader.ReadString('\n') //readstring 的参数是byte, go里面byte是单引号
		// EOF 表示读完了
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println("read string failed, err:", err)
			break
		}

		runeArr := []rune(str)
		for _, v := range runeArr {
			switch {
			case v >= 'a' && v <= 'z':
				fallthrough
			case v >= 'A' && v <= 'Z':
				count.CharCnt++
			case v == ' ' || v == '\t':
				count.SpaceCnt++
			case v >= '0' && v <= '9':
				count.NumCnt++
			default:
				count.OtherCnt++

			}
		}
	}
	fmt.Println(count)
}
