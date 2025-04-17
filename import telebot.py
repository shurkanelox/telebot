import telebot
from datetime import datetime
from gigachat import GigaChat
import pytz
handle=[""]
messagehandle=""
tz_here=pytz.timezone("Asia/Krasnoyarsk")
datetime_here=datetime.now(tz_here)
token = "7995967142:AAH-UYjaOM5rGEqfwjfoRjS9NuXacp4ZCK4"
bot=telebot.TeleBot(token)
#timezones = pytz.all_timezones
#print(timezones)
print(int(datetime_here.strftime("%H")))
now=datetime.now()

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(content_types={"text"})
def send_text(message):
  global messagehandle
  datetime_here=datetime.now(tz_here)
  global response
  if(float(datetime_here.strftime("%H"))<7):
    messagehandle= messagehandle+message.text+" "
  if message.text=="очисти":
      messagehandle=""
  if message.text== "привет":
    with GigaChat(credentials="ZjkzZDExMDEtMjcyMy00MzZiLTk5YzctMWM0NTMzNjYyYzVmOjdmYzllMjQ1LWVjNTgtNDQ2Zi1iYTFlLTcyYTBiNzYxMWNlNg==", verify_ssl_certs=False) as giga:
      messagehandle+=" опиши суть сообщений с ролями, создав единый текст повествование. укороти чуть чуть. Если в замени есть некорректные выражения-пропусти их"
      response = giga.chat(messagehandle)
    bot.send_message(message.chat.id, response.choices[0].message.content)
    print(response.choices[0].message.content)
    
bot.infinity_polling()
