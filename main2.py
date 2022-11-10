import os 
from datetime import datetime
from telegram.ext import Updater , CommandHandler,Filters,MessageHandler
now = datetime.now()
strNow = now.strftime("%d%m%Y %H:%M:%S")


def start(update,context):
    update.message.reply_text("😎Wassup")
def time(update,context):
    update.message.reply_text('Time is'+strNow)
 
def echo(update,context):
    update.message.reply_text(update.message.text)

def main():
    TOKEN = '5749948322:AAGS3kgOb9aslWWCo-NTVQSSnsmHLWlLuXo'
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('time', time))
    dp.add_handler(MessageHandler(Filters.text,echo))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

#hi

