from handlers import staticFiles

def routeRequest(req):
    method = req.method
    path   = req.path
    reqFile = staticFiles.fileExists(path)

    if reqFile:
       return staticFiles.loadResource(reqFile)
    else:
         return {
            "status_code": 404,
            "headers": {"Content-type": "text/plain: charset=UTF-8"},
            "body": "Not Found",
        }
       