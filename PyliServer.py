import socket
import sys
import os
import ConfigParser

import RequestHandler


def parseConfigs(configFile):
    configMap = {}
    config = ConfigParser.ConfigParser()
    config.read(configFile)
    configMap.update({'webdir':config.get('Webdirectory', 'directory')})
    configMap.update({'host':config.get('Host', 'hostname')})
    configMap.update({'port':config.get('Port', 'listenport')})
    return configMap


def createServerSocket():
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return listenSocket

def handleRequest(clientSocket, configs):
    request = clientSocket.recv(1024)
    try:
        getLine = request.splitlines()[0]
        (method, path, version) = getLine.split()

        rqstHandle = RequestHandler.RequestHandler(configs)

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



def serverStart(listenSocket, configs):
    hostname = configs['host']
    port = int(configs['port'])

    listenSocket.bind((hostname, port))
    listenSocket.listen(5)

    print "Server started at %s : %s" % (hostname, port)

    while True:
        clientSocket, clientAddress = listenSocket.accept()

        pid = os.fork()
        if pid == 0:
            listenSocket.close()
            handleRequest(clientSocket, configs)
            os._exit(0)
        else:
            clientSocket.close()


def main():
    serverSocket = createServerSocket()
    configs = parseConfigs('pyli.conf')

    serverStart(serverSocket, configs)


if __name__ == '__main__':
    main()
