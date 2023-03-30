from handlers import staticFiles

ROUTES = {
    "GET": {
        "/": staticFiles.index,
        "/css/style.css": staticFiles.style,
    }
}

def routeRequest(req):
    method = req.method
    path   = req.path

    handler = ROUTES.get(method, {}).get(path)

    if handler:
        return handler(req)
    else:
        return {
            "status_code": 404,
            "headers": {"Content-type": "text/plain: charset=UTF-8"},
            "body": "Not Found",
        }