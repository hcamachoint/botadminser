https://github.com/eternnoir/pyTelegramBotAPI
-------------------------------------------------

$ sudo apt update
$ sudo apt-get install supervisor
$ sudo supervisord

$ sudo mkdir /var/log/telebotpy
$ sudo cp main.conf /etc/supervisor/conf.d/

$ sudo supervisorctl reread
$ sudo supervisorctl update

-------------------------------------------------

$ pip3 install -r requirements.txt
$ cp .env.example .env
$ python3 main.py

-------------------------------------------------

$ sudo supervisorctl stop botadminser-main
$ sudo supervisorctl start botadminser-main
$ sudo supervisorctl restart botadminser-main
$ sudo supervisorctl status botadminser-main

-------------------------------------------------

$ sudo tail -f logfile.log
