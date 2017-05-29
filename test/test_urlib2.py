'''
Created on May 28, 2017

@author: Dave
'''
import urllib2
import cookielib

url = "http://www.baidu.com"

print 'method 1'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print 'method 2'
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print 'method 3'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request)
print response3.getcode()
print response3.read()