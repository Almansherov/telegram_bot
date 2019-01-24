from __future__ import unicode_literals
import time
import telepot
import requests
import os, sys
import youtube_dl
from pydl import MyLogger, my_hook, ydl_opts
import re


TOKEN = "your_token"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    input_text = msg['text']
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)
    path = '/home/alman/telegram_bot'
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', input_text)
    url = str(url)
    url = url.replace('[', '')
    url = url.replace("'", '')
    url = url.replace(']', '')
    print(url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        bot.getUpdates
        files = os.listdir(path)
        for file in files:
            if ".mp3" in file:
                url = "https://api.telegram.org/bot%s/sendAudio"%(TOKEN)
                files = {'audio': open(file, 'rb')}
                data = {'chat_id' : chat_id}
                r= requests.post(url, files=files, data=data)
                print(r.status_code, r.reason, r.content)
                os.remove(file)
    # else:
    #     bot.sendMessage(chat_id,text = "This is not a proper usage of me. Please, send me a message that contains youtube URL and I will send it back to you.")
        


bot = telepot.Bot("your_token")
bot.message_loop(handle)

print('Listening ...')

while 1:
    time.sleep(10)


