#!/bin/bash

cd /home/ubuntu/quasarzoneAutoBot/

echo "" >> runBot.log
date +%Y-%m-%d_%T >> runBot.log
pwd >> runBot.log

python3 - << 'EOF'

from auto_post_update import PostBot
from auto_attendance_check import AttChkBot

login_info = {
    'USER_ID': "abcd",
    'USER_PASSWORD_1': "abcd",
    'USER_PASSWORD_2': "abcd",
}

if __name__ == '__main__':
    attendance_success = AttChkBot(login_info).att_check()

    if attendance_success:
        PostBot(True, login_info).post_update()
    else:
        PostBot(False, login_info).post_update()

EOF
