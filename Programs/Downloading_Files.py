import random
import urllib.request

def downloadFile(url):
    if '.jpg' in url:
        fileType = '.jpg'

    elif '.zip' in url:
        fileType = '.zip'

    else:
        print("This program doesn't currently support that kind of file")

    name = random.randrange(1, 1000)
    fullName = str(name) + fileType
    urllib.request.urlretrieve(url, fullName)

    print("Done!")

    redo = input("Would you like to download another file? (Y/N): ")
    if redo is 'y':
        downloadFile(url = input("Input url here: "))
    else:
        return print("Thank you!")

downloadFile(url = input("Input url here: "))

