#!/usr/bin/env python 
# coding: utf-8 
import sys 
import urllib 
import urllib2 
URL = 'http://web.cr6868.com/asmx/smsservice.aspx?name=18910329939&pwd=DDFD1D01C3F8E4A8EF0A4290E1D1&' 
#ID = '109591' 
ID = 'pt'
def sendsms(pho,title,content): 
    u1 = title.decode('utf-8') 
    u2 = content.decode('utf-8') 
    title = u1.encode('utf-8') 
    content = u2.encode('utf-8') 
    msm = {'mobile':pho, 'content':title + content, 'type':ID} 
    body = urllib.urlencode(msm) 

    request = URL+body 
    # body = urllib.urlencode(request) 
    urldata = urllib2.urlopen(request) 
    print(request) 
    print(urldata.read()) 
    print(content) 
if __name__ == '__main__': 
    sendsms(sys.argv[1], str(sys.argv[2]), str(sys.argv[3]))
