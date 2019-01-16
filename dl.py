from __future__ import unicode_literals
import time
import telepot
import requests
import os, sys
import youtube_dl
from pydl import MyLogger, my_hook, ydl_opts

TOKEN = "760565322:AAF_i401TKDPb67A7PJStDF8drYs-4z-x3w"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    input_text = msg['text']
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)
    path = '/home/alman/telegram_bot'
    

    if input_text.startswith("https://"):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([input_text])
            files = os.listdir(path)
            for file in files:
                if ".mp3" in file:
                    url = "https://api.telegram.org/bot%s/sendAudio"%(TOKEN)
                    files = {'audio': open(file, 'rb')}
                    data = {'chat_id' : chat_id}
                    r= requests.post(url, files=files, data=data)
                    print(r.status_code, r.reason, r.content)
                    os.remove(file)

    else:
        bot.sendMessage(chat_id,text = "This is not a proper usage of me. Please, make sure to send me a URL that starts exactly with https://. I have not learnt to read the links inside of the messages yet.")

bot = telepot.Bot("760565322:AAF_i401TKDPb67A7PJStDF8drYs-4z-x3w")
bot.message_loop(handle)
print('Listening ...')

while 1:
    time.sleep(10)