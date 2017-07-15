import os
import getpass
import subprocess as sp
from sys import stdout


def download_data():
    """Uses youtube_dl to download individual json files for each video."""
    print('There\'s no data in this folder. Let\'s download some.')
    successful_login = False
    while not successful_login:
        successful_login = True
        user = input('Google username: ')
        pw = getpass.getpass('Google password: ')
        files = os.path.join(self.raw, '%(autonumber)s')
        if not os.path.exists(self.raw):
            os.makedirs(self.raw)
            cmd = ('youtube-dl -u "{}" -p "{}" '+
            '-o "{}" '+
            '--skip-download --write-info-json -i '+
            'https://www.youtube.com/feed/history ').format(user, pw, files)
            p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.STDOUT, shell=True)
            while True:
                line = p.stdout.readline().decode("utf-8").strip()
                print(line)
                if line == 'WARNING: unable to log in: bad username or password':
                    successful_login = False
                    if not line: break
