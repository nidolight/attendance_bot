import requests
from bs4 import BeautifulSoup
from datetime import datetime


class PostBot:
    url_login = "http://193.123.225.81/accounts/login/"
    update_post_url = "http://193.123.225.81/blog/update_post/13/"

    def __init__(self, attendance_success, login_info):
        self.attendance_success = attendance_success
        self.USER_ID = login_info['USER_ID']
        self.USER_PASSWORD = login_info['USER_PASSWORD_2']

    def post_update(self):
        with requests.Session() as session:
            with session.get(self.url_login) as response:
                soup = BeautifulSoup(response.text, features='html.parser')
                csrf = soup.find_all('input', attrs={'type': 'hidden'})[0]

                header = {
                    "Referer": self.url_login,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
                }
                data = {
                    csrf['name']: csrf['value'],
                    "login": self.USER_ID,
                    "password": self.USER_PASSWORD
                }

            # Login
            session.post(self.url_login, headers=header, data=data)

            with session.get(self.update_post_url) as response2:
                soup = BeautifulSoup(response2.text, features='html.parser')
                form = soup.find('div', attrs={'id': 'main-area'})
                auth = form.find_all('input', attrs={'type': 'hidden'})[0]

                content = form.find('textarea', attrs={'id': 'id_content'})
                date_now = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
                cum_num = int(content.text[-2])

                if self.attendance_success:
                    new_content = content.text + '<br>' + '\n - ' + date_now + f' - 누적 출석 일수 : {cum_num + 1}일'
                else:
                    new_content = content.text + '<br>' + '\n - ' + date_now + f' 실패!!! - 누적 출석 일수 : 0일'

                header = {
                    "Referer": self.update_post_url,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
                }
                data = {
                    auth['name']: auth['value'],
                    'title': '🤖 퀘이사존 자동출첵봇',
                    'hook_text': '',
                    'content': new_content,
                    'head_image': '',
                    'file_upload': '',
                    'category': '',
                    'tags_str': ''
                }

            # Update Post
            session.post(self.update_post_url, headers=header, data=data)
