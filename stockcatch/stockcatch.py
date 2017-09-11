import urllib.request
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    codes = ['035420', '054920', '215600']
    for code in codes:
        urlstring = "http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code=" + code
        req = urllib.request.Request(urlstring)
        data = urllib.request.urlopen(req).read().decode("utf-8")

        # print (data)
        tree = ET.fromstring(data.replace('\n',''))
        print(tree.find('TBL_StockInfo').attrib['JongName'],tree.find('TBL_StockInfo').attrib['CurJuka'], )
