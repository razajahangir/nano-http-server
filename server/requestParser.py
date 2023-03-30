class requestParser:

    def __init__(self, method, path, http_version, headers, body):
        self.method       = method
        self.path         = path
        self.http_version = http_version
        self.headers      = headers
        self.body         = body

    def parseRequest(reqBytes):
        reqStr = reqBytes.decode("utf-8")
        reqLines = reqStr.split("\r\n")

        method, path, http_version = reqLines[0].split(" ", 2)
        headers = {}
        body = ""

        for line in reqLines[1:]:
            if line == "":
                break
            headerName, headerValue = line.split(": ", 1)
            headers[headerName] = headerValue

        if len(reqLines) > len(headers) + 2:
            body = reqLines[len(headers) + 2]

        return requestParser(method, path, http_version, headers, body)