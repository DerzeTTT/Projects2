import requests


tUrl = 'http://httpbin.org/html'
headers = {

    'HOST':'httpbin.org',
    'User-Agent':'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'

}

returned = requests.get(tUrl, headers=headers)

newFile = open("test.html", "w")
newFile.write(returned.content.decode('utf-8'))

newFile.close()