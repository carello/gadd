
import requests

requests.packages.urllib3.disable_warnings()

'''
Copy this file to a new file called `creds.py` and make changes as needed.
Set static credentials for demo
Ideally this would be inputted via env at runtime
'''


lg_inp = "<user_login_name>"
ps_inp = "<user_password>"
url_inp = "<url_to_device>"
tk_inp = "Bearer <spark room token>"
rm_inp = "<TBD: future place holder>"


def nvfis_getgcred():
    login = lg_inp
    password = ps_inp
    url = url_inp
    return url, login, password


def spark_GetArgs():
    token = tk_inp
    # add other variables as needed and return
    return token
