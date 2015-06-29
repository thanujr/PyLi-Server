import os


class RequestHandler:

    def __init__(self, configs):
        self.webDirectory = configs['webdir']

    def handleGETMethod(self, path):
        resourcePath = self.webDirectory + path

        if os.path.exists(resourcePath):
            try:
                header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n'
                content = open(resourcePath, 'rb').read()
            except:
                header = 'HTTP/1.1 500 Internal Server Error\r\n\r\n'
                content = '<html><body><h1>Internal Server Error</h1></body></html>'
        else:
            header = 'HTTP/1.1 404 NotFound\r\n\r\n'
            content = '<html><body><h1>File Not Found.</h1></body></html>'

        return header + content

    def handleHEADMethod(self, path):
        resourcePath = self.webDirectory + path

        if os.path.exists(resourcePath):
            try:
                header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n'
            except:
                header = 'HTTP/1.1 500 Internal Server Error\r\n\r\n'
        else:
            header = 'HTTP/1.1 404 NotFound\r\n\r\n'

        return header

    def handlePOSTMethod(self, request):
        postBody = request.split("\r\n\r\n")[1]
        params = postBody.split('&')

        content = 'POST Data: '

        for item in params:
            content += item
            content += ','


        header = 'HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n\r\n'

        return header + content


    def throwBadRequestError(self):
        return 'HTTP/1.1 400 Bad Request\r\n'
