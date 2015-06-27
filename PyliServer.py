import socket
import sys
import os


WEBDIRECTORY = 'www'


def createServerSocket():
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return listenSocket


def handleGETMethod(path):
    resourcePath = WEBDIRECTORY + path

    if os.path.exists(resourcePath):
        try:
            header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n'
            content = open(resourcePath, 'rb').read()
        except:
            header = 'HTTP/1.1 404 NotFound\r\n\r\n'
            content = 'Content Not Found!'
    else:
        header = 'HTTP/1.1 404 NotFound\r\n\r\n'
        content = 'Content Not Found!'

    return header + content


def handleHEADMethod():
    pass


def handlePOSTMethod():
    pass


def serverStart(listenSocket, hostname, port):
    listenSocket.bind((hostname, port))
    listenSocket.listen(5)

    print "Server started at %s : %s" % (hostname, port)

    while True:
        clientSocket, clientAddress = listenSocket.accept()
        request = clientSocket.recv(1024)

        print request

        getLine = request.splitlines()[0]
        (method, path, version) = getLine.split()

        if(method == 'GET'):
            response = handleGETMethod(path)


        clientSocket.sendall(response)
        clientSocket.close()


def main():
    args = sys.argv[1:]

    if len(args) == 2:
        serverSocket = createServerSocket()
        serverStart(serverSocket, args[0], int(args[1]))


if __name__ == '__main__':
    main()
