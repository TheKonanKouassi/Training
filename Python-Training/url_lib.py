from urllib import request, parse

link = request.urlopen('https://www.google.com')

# print(link.read())

url = 'https://pythonprogramming.net'

values = {'q' : 'basic'}

data = parse.urlencode(values)

data = data.encode('utf-8')

req = request.Request(url = url, data = data)

reps = request.urlopen(req)

respData = reps.read()

#print(respData)

try:
    x = request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    data = {'safe' : 'safe=off&dcr=0&source=hp&ei=wNxMWve8BIycmwGj3YOoDA&q=test&oq=test&gs_l=psy-ab.3..35i39k1l2j0i67k1l2j0l2j0i67k1j0l3.3170.3487.0.4775.6.4.0.0.0.0.617.617.5-1.1.0....0...1.1.64.psy-ab..5.1.617.0...0.LJ6yEdA1uE4'}
    req = request.Request(url = url, data = data)
    reps = request.urlopen(req)
    try:
        with open('WithHeaders.txt', 'w') as saveFile:
            saveFile.write(str(reps))
    except Exception as e:
        print(str(e))
except Exception as e:
    print(str(e))





