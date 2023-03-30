STATUS_CODES = {
    200: "OK",
    201: "Created",
    400: "Bad Request",
    404: "Not Found",
    500: "Internal Server Error",
}

def buildResponse(res):
    status_code = res["status_code"]
    status_message = STATUS_CODES.get(status_code, "Unknown")
    headers = res["headers"]
    body = res["body"]

    # Build the status line
    status_line = f"HTTP/1.1 {status_code} {status_message}"

    # Build the headers
    headers_str = "\r\n".join([f"{key}: {value}" for key, value in headers.items()])

    # Build the final HTTP response
    http_response = f"{status_line}\r\n{headers_str}\r\n\r\n{body}".encode("utf-8")

    return http_response
