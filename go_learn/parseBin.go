package main

import (
	"fmt"
	"log"
	"os"
)

type Header struct {
	UserDataMaxSize uint32
	HeaderOffset    uint32
	UserDataSize    uint32
	_               [5]byte
	Starcraft2      [22]byte
}

func main() {
	path := "heptio-e2e.test"

	file, err := os.Open(path)
	if err != nil {
		log.Fatal("Error while opening file", err)
	}

	defer file.Close()

	fmt.Printf("%s opened\n", path)

	formatName := readNextBytes(file, 1000)
	fmt.Printf("Parsed info: %s\n", formatName)

	// if string(formatName) != "MPQ\x1b" {
	// 	log.Fatal("Provided replay file is not in correct format.")
	// }

	// header := Header{}
	// data := readNextBytes(file, 39) // 4 * uint32 (3) + 5 * byte (1) + 22 * byte (1) = 43

	// buffer := bytes.NewBuffer(data)
	// err = binary.Read(buffer, binary.LittleEndian, &header)
	// if err != nil {
	// 	log.Fatal("binary.Read failed", err)
	// }

	// fmt.Printf("Parsed data:\n%+v\n", header)
}

func readNextBytes(file *os.File, number int) []byte {
	bytes := make([]byte, number)

	_, err := file.Read(bytes)
	if err != nil {
		log.Fatal(err)
	}

	return bytes
}
