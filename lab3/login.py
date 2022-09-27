#!/usr/bin/env python3
import cgi
import secret
import os
from templates import secret_page

form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")
body = ""

def parse_cookies(cookie_string):
    result = {}
    keyvaluepairs = cookie_string.split(";")
    for pair in keyvaluepairs:
        key, value = pair.split("=")
        result[key] = value

    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])
if cookies["logged"] == "true":
    body += secret_page(secret.username, secret.password)

elif username == secret.username and password == secret.password:
    header += "Set-Cookie: logged=true;\r\n"
    header += "Set-Cookie: test=test;\r\n"


header = ""
header += "Content-Type: text/html\r\n"

print(header)
print(body)
