package main

import (
	"bufio"
	"log"
	"net"
)

// TCPClient holds info about connection
type TCPClient struct {
	Conn             net.Conn
	Server           *TCPServer
	RecvSize         int
	SendSize         int
	ClientNewMessage func(c *TCPClient, message []byte, tid int) (ifClose bool, err error)
}

// TCP server
type TCPServer struct {
	clients                  []*TCPClient
	address                  string // Address to open connection: localhost:9999
	onNewClientCallback      func(c *TCPClient)
	onClientConnectionClosed func(c *TCPClient, err error)
	onNewMessage             func(c *TCPClient, message []byte, tid int) (ifClose bool, err error)
}

// Read client data from channel
func (c *TCPClient) listen(tid int) {
	var buf []byte
	var ifClose bool

	msgSize := c.RecvSize
	buf = make([]byte, msgSize)
	reader := bufio.NewReader(c.Conn)
	for {
		n, err := reader.Read(buf)
		if err != nil || n != msgSize {
			c.Conn.Close()
			c.Server.onClientConnectionClosed(c, err)
			return
		}
		//###c.Server.onNewMessage(c, buf)
		ifClose, err = c.ClientNewMessage(c, buf, tid)
		if ifClose == true || err != nil {
			c.Conn.Close()
			c.Server.onClientConnectionClosed(c, err)
			return
		}
		/*
			message, err := reader.ReadString('\n')
			if err != nil {
				c.Conn.Close()
				c.Server.onClientConnectionClosed(c, err)
				return
			}
			c.Server.onNewMessage(c, message)
		*/
	}
}

// Send text message to client
func (c *TCPClient) Send(message string) error {
	_, err := c.Conn.Write([]byte(message))
	return err
}

// Send bytes to client
func (c *TCPClient) SendBytes(b []byte) error {
	_, err := c.Conn.Write(b)
	return err
}

func (c *TCPClient) Close() error {
	return c.Conn.Close()
}

// Called right after server starts listening new client
func (s *TCPServer) OnNewClient(callback func(c *TCPClient)) {
	s.onNewClientCallback = callback
}

// Called right after connection closed
func (s *TCPServer) OnClientConnectionClosed(callback func(c *TCPClient, err error)) {
	s.onClientConnectionClosed = callback
}

// Called when TCPClient receives new message
func (s *TCPServer) OnNewMessage(callback func(c *TCPClient, message []byte, tid int) (ifClose bool, err error)) {
	s.onNewMessage = callback
}

// Start network server
func (s *TCPServer) Listen() {
	listener, err := net.Listen("tcp", s.address)
	if err != nil {
		log.Fatal("Error starting TCP server.")
	}
	defer listener.Close()

	tid := 0
	for {
		tid += 1
		conn, _ := listener.Accept()
		client := &TCPClient{
			Conn:             conn,
			Server:           s,
			ClientNewMessage: s.onNewMessage,
		}
		go client.listen(tid)
		s.onNewClientCallback(client)
	}
}

// Creates new tcp server instance
func TCPServerNew(address string) *TCPServer {
	log.Println("Creating server with address", address)
	server := &TCPServer{
		address: address,
	}

	server.OnNewClient(func(c *TCPClient) {})
	server.OnNewMessage(func(c *TCPClient, message []byte, tid int) (ifClose bool, err error) { return ifClose, err })
	server.OnClientConnectionClosed(func(c *TCPClient, err error) {})

	return server
}
