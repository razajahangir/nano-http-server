import os

def loadResource(reqFile):
    with open(reqFile, "r") as file:
        content = file.read()
    return {
        "status_code": 200,
        "headers": {"Content-Type": "text/html; charset=UTF-8"},
        "body": content,
    }

def fileExists(filePath):
    publicDir  = '/var/www' # Will be fetched from config file later
    filePath = publicDir + filePath
    if os.path.isfile(filePath):
        return filePath
    else:
        return False

