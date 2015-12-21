import random
import urllib.request

def downloadImage(url):
    if '.jpg' in url:
        fileType = '.jpg'

    elif '.gif' in url:
        fileType = '.gifv'

    else:
        return print("That is not an image")

    name = random.randrange(1, 1000)
    fullName = str(name) + fileType
    urllib.request.urlretrieve(url, fullName)

    print("Done!")

downloadImage(url = input("Input URL here: "))
