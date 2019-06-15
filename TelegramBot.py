import telebot
import time
bot_token="Your bot token here"
bot=telebot.TeleBot(token=bot_token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome! For further instructions type /help.Type /credits to view the developer info')
@bot.message_handler(commands=['credits'])
def credits(message):
    bot.reply_to(message,'your url')
    time.sleep(1)
    bot.reply_to(message,'your url')
    time.sleep(1)
    bot.reply_to(message,'your url')
    time.sleep(1)
    bot.reply_to(message,'your telegram id')
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'There are following sites available to download. To use the sites just type the series name followed by the command.\nThe commands are \n/480mkv -Site is 480mkv \n/indexof - Uses google to search the link\n/pb - piratebay proxy\n/anime - to get dubbed anime\nEg. the flash /480mkv')
@bot.message_handler(func=lambda msg: msg.text is not None  and '/480mkv' in msg.text)
def _480mkv(message):
    texts=message.text.split()
    string=''
    for i in texts:
        if '/480mkv' in i:
            break
        string=string+'-'+i
    bot.reply_to(message,'https://www.480mkv.com/category/{}'.format(string[1:]))
@bot.message_handler(func=lambda msg:msg.text is not None and '/indexof' in msg.text)
def indexof(message):
    texts=message.text.split()
    string=''
    for i in texts:
        if '/indexof' in i:
            break
        string=string+'+'+i
    bot.reply_to(message,'https://www.google.com/search?q=indexof+{}'.format(string[1:]))
@bot.message_handler(func=lambda msg:msg.text is not None and '/pb' in msg.text)
def piratebay(message):
    texts=message.text.split()
    string=''
    for i in texts:
        if '/pb' in i:
            break
        string=string+'+'+i
    bot.reply_to(message,'https://proxy247.art/s/?q={}'.format(string[1:]))
@bot.message_handler(func=lambda msg:msg.text is not None and '/anime' in msg.text)
def piratebay(message):
    texts=message.text.split()
    string=''
    for i in texts:
        if '/anime' in i:
            break
        string=string+'+'+i
    bot.reply_to(message,'https://www.animeland.us/?s={}'.format(string[1:]))
bot.polling()
   
