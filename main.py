import os
import time
import logging
import subprocess
import telebot
from datetime import datetime
from dotenv import load_dotenv

#LOGGIN CONFIG
logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
logger.addHandler(handler)
logger.setLevel(level=logging.INFO)

load_dotenv()   #ENV CONFIG
bot = telebot.TeleBot(os.getenv('apikey'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	logger.info('#'+str(datetime.now()) + ' - MESSAGE: ' + str(message))
	bot.reply_to(message, "😺 Use commands: /start, /help")

@bot.message_handler(commands=['apache_hosts'])
def apache_hosts(message):
	logger.info('#'+str(datetime.now()) + ' - MESSAGE: ' + str(message))
	output = subprocess.getoutput("sudo apache2ctl -S 2>&1 | grep 'port 80' | awk '/namevhost/  {print $4;} '")
	if not output:
		bot.reply_to(message, 'Nothing to show')
	else:
		bot.reply_to(message, output)

@bot.message_handler(commands=['server_status'])
def server_status(message):
	logger.info('#'+str(datetime.now()) + ' - MESSAGE: ' + str(message))
	apache = subprocess.getoutput("sudo systemctl status apache2")
	mysql = subprocess.getoutput("sudo systemctl status mysql")
	postgresql = subprocess.getoutput("sudo systemctl status postgresql")
	
	bot.reply_to(message, apache)
	bot.reply_to(message, mysql)
	bot.reply_to(message, postgresql)

bot.infinity_polling()