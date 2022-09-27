#!/usr/bin/env python3
import os
import json
from templates import login_page 


env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value

# print("Content-Type: application/json") 
# print()

# print(json.dumps(env))
# print(env["QUERY_STRING"])
# print(env["HTTP_USER_AGENT"])

print("Content-Type: text/html\r\n") 
print()
print(login_page())

