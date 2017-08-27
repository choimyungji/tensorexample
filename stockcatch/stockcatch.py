import urllib.request

if __name__ == "__main__":
    urlstring = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code=035420"
    req = urllib.request.Request(urlstring)
    data = urllib.request.urlopen(req).read()

    print (data)
