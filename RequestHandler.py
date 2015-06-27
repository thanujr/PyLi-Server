import os


class RequestHandler:

    def __init__(self):
        self.webDirectory = 'www'
        pass

    def handleGETMethod(self, path):
        resourcePath = self.webDirectory + path

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

    def handleHEADMethod(self, path):
        resourcePath = self.webDirectory + path

        if os.path.exists(resourcePath):
            try:
                header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n'
            except:
                header = 'HTTP/1.1 404 NotFound\r\n\r\n'
        else:
            header = 'HTTP/1.1 404 NotFound\r\n\r\n'

        return header

    def handlePOSTMethod(self, request):
        postBody = request.split("\r\n\r\n")[1]
        params = postBody.split('&')


        postParams = {}
        content = 'POST Data: '

        for item in params:
            content += item
            content += ','


        header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n'

        return header + content
