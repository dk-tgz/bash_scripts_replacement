// 2>/dev/null;/usr/bin/go run "$0" "$@"; exit $?
package main

import (
	"log"
	"fmt"
	//   "github.com/bitfield/script"
	"github.com/melbahja/goph"
	"golang.org/x/crypto/ssh"
)

func main() {

	// Start new ssh connection with private key.
	auth, err := goph.Key("../../ssh/id_rsa", "")
	if err != nil {
		log.Fatal(err)
	}
        config := goph.Config{
		Auth: auth,
		Port: 2222,
		User: "ubuntu",
		Addr: "localhost",
		Callback: ssh.InsecureIgnoreHostKey(),
	}
	client, err := goph.NewConn(&config)
	if err != nil {
		log.Fatal(err)
	}

	// Defer closing the network connection.
	defer client.Close()

	// Execute your command.
	out, err := client.Run("sudo touch /etc/test")

	if err != nil {
		log.Fatal(err)
	}

	// Get your output as []byte.
	fmt.Println(string(out))

	out, err = client.Run("ls /etc/test")

	if err != nil {
		log.Fatal(err)
	}

	// Get your output as []byte.
	fmt.Println(string(out))

	out, err = client.Run("sudo rm -rf /etc/test")

	if err != nil {
		log.Fatal(err)
	}

	// Get your output as []byte.
	fmt.Println(string(out))

	out, err = client.Run("ls -lrt /etc/test")

	if err != nil {
		log.Fatal(err)
	}

	// Get your output as []byte.
	fmt.Println(string(out))
}
