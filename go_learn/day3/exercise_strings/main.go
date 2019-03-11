// strings 包常用函数
// strings.Index()
// strings.LastIndex()
// strings.Replace()
// strings.Count
// strings.Repeat
// strings.ToLower
// strings.ToUpper
// strings.TrimSpace 去掉首位空白字符 strings.Trim, strings.TrimLeft, strings.TrimRight
// strings.Field(str string) 返回str字符串以空白分隔的所有子串的slice
// strings.Split, strings.Join
// strings.Itoa(i int) 把整数转换成字符串; strings.Atoi(str string) (int error)

package main

import (
	"fmt"
	"strings"
)

func urlProcess(url string) string {
	result := strings.HasPrefix(url, "http://")
	if !result {
		url = fmt.Sprintf("http://%s", url)
	}
	return url
}

func pathProcess(path string) string {
	result := strings.HasSuffix(path, "/")
	if !result {
		path = fmt.Sprintf("%s/", path)
	}
	return path
}

func main() {
	var (
		url  string
		path string
	)

	fmt.Scanf("%s%s", &url, &path)
	url = urlProcess(url)
	path = pathProcess(path)

	fmt.Println(url)
	fmt.Println(path)
}
