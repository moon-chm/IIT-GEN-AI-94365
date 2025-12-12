def gettemp(response):
    return response['main']['temp']

def gethumidity(response):
    return response['main']['humidity']

def getwind(response):
    return response['wind']['speed']

def gettimezone(response):
    return response['timezone']
