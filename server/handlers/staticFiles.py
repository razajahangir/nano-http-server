def index(request):
    with open("static/index.html", "r") as file:
        content = file.read()
    return {
        "status_code": 200,
        "headers": {"Content-Type": "text/html; charset=UTF-8"},
        "body": content,
    }

def style(request):
    with open("static/css/style.css", "r") as file:
        content = file.read()
    return {
        "status_code": 200,
        "headers": {"Content-Type": "text/css; charset=UTF-8"},
        "body": content,
    }

# Add more static file handlers as needed
