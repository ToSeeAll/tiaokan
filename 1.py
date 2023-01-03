import time
import re
import requests
import urllib3
import os


def login(user, passwd):
    headers = {
        'authority': 'tiaokan.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'PHPSESSID=rdo03vkck3fnp82ugafmnfsh0o; wordpress_test_cookie=WP+Cookie+check',
        'origin': 'https://tiaokan.org',
        'referer': 'https://tiaokan.org/wp-login.php',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    }

    data = {
        'log': user,
        'pwd': passwd,
        'wp-submit': '登录',
        'redirect_to': 'https://tiaokan.org/wp-admin/',
        # 'testcookie': '1',
    }
    sessions = requests.session()
    response = sessions.post('https://tiaokan.org/wp-login.php', headers=headers, data=data, verify=False)
    if '跳转' in response.text:
        link=re.findall('href ="(.*?)"',response.text)
        link=link[0]
        response2 = sessions.post('https://tiaokan.org'+link, headers=headers, data=data, verify=False)

    headers = {
        'authority': 'tiaokan.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://tiaokan.org',
        'referer': 'https://tiaokan.org/user?pd=money',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'epd_checkin',
    }

    response =sessions.post('https://tiaokan.org/wp-admin/admin-ajax.php', cookies=sessions.cookies, headers=headers,
                             data=data, verify=False)
    msg = response.text

    print( msg.encode('utf-8').decode('unicode_escape'))


if __name__ == '__main__':
    urllib3.disable_warnings()
    USER1=os.environ['USER1']
    PW1=os.environ['PW1']
    USER2=os.environ['USER2']
    PW2=os.environ['PW2']
    accounts = [[USER1,PW1],[USER2,PW2]]
    for account in accounts:
        user, passwd = account
        login_url = 'https://tiaokan.org/wp-login.php'
        login(user, passwd)

        time.sleep(5)
