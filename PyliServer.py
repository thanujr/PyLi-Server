import socket
import sys
import os

import RequestHandler


def createServerSocket():
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return listenSocket


def serverStart(listenSocket, hostname, port):
    listenSocket.bind((hostname, port))
    listenSocket.listen(5)

    print "Server started at %s : %s" % (hostname, port)

    while True:
        clientSocket, clientAddress = listenSocket.accept()
        request = clientSocket.recv(1024)

        print request

        try:
            getLine = request.splitlines()[0]
            (method, path, version) = getLine.split()

            rqstHandle = RequestHandler.RequestHandler()

            if(method == 'GET'):
                response = rqstHandle.handleGETMethod(path)

            if(method == 'HEAD'):
                response = rqstHandle.handleHEADMethod(path)

            if(method == 'POST'):
                response = rqstHandle.handlePOSTMethod(request)

            clientSocket.sendall(response)
            clientSocket.close()

        except:
            clientSocket.close()


def main():
    args = sys.argv[1:]

    if len(args) == 2:
        serverSocket = createServerSocket()
        serverStart(serverSocket, args[0], int(args[1]))


if __name__ == '__main__':
    main()
