from urllib2 import urlopen
from HTMLParser import HTMLParser

class ImageParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag != 'img':
			return
		if not hasattr(self, 'result'):
			self.result = []
		for name, value in attrs:
			if name == 'src':
				self.result.append(value)

def parseImage(data):
	parser = ImageParser()
	parser.feed(data)
	dataSet = set(x for x in parser.result)
	print '\n'.join( sorted(dataSet) )

def main():
	url = "http://www.daum.net"

	f = urlopen(url)
	charset = f.info().getparam('charset')
	data = f.read().decode(charset)
	f.close()

	print "\n>>>>>>>>>> Fetch Images from", url
	parseImage(data)

if __name__ == '__main__':
	main()

# auth_handler = urllib2.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',uri='https://mahler:8092/site-updates.py',user='klem',passwd='kadidd!ehopper')
# opener = urllib2.build_opener(auth_handler)

# urllib2.install_opener(opener)
# u = urllib2.urlopen('http://www.example.com/login.html')
