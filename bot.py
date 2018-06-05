import time
import const
import telegram as tg
import telegram.ext as tgext
import skimage
from skimage.feature import hog
import numpy as np
from sklearn.externals import joblib

cls = joblib.load('cls.pkl')
people_size = (62, 47)


def search(filepath):
    print('1')
    img = skimage.io.imread(filepath)
    print('2')
    rects = list()
    print('3')
    print(img)
    print('4')
    print(type(img))
    print('5')


    return cls.predict(hog(img[:, :, 2]))


bot_updater = tgext.Updater(token=const.token)
bot_dispatcher = bot_updater.dispatcher


def start(bot, update):
    print("/start send by ", update.message.chat.username)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Hello! I'm a simple bot written by @randomdanil\nU can see what i do using /info\n"
                          "U can see manual using /help")
    print(update)


def bot_help(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=tg.ChatAction.TYPING)
    time.sleep(1)
    print("/help send by ", update.message.chat.username)
    bot.send_message(chat_id=update.message.chat_id, text="help message")


def info(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=tg.ChatAction.TYPING)
    # time.sleep(1)
    print("/info send by ", update.message.chat.username)
    bot.send_message(chat_id=update.message.chat_id, text="send photo to locate face on it")


def picture(bot, update):
    print("photo send by ", update.message.chat.username)
    # bot.send_chat_action(chat_id=update.message.chat_id, action=tg.ChatAction.TYPING)
    # time.sleep(1)
    # bot.send_message(chat_id=update.message.chat_id, text="working on it")
    # print(update.message)
    filename = bot.getFile(file_id=update.message.photo[-1].file_id).download(
        custom_path='photos\\' + str(update.message.message_id) + '-' + str(update.message.chat.username) + ".png")
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    f = search(filename)
    """
    try:
        f = search(filename)
    except Exception:
        f = 0
    """
    bot.send_chat_action(chat_id=update.message.chat_id, action=tg.ChatAction.TYPING)

    if f == 0:
        bot.send_message(chat_id=update.message.chat_id, text='i found 0 faces')
    else:
        if f == 1:
            bot.send_message(chat_id=update.message.chat_id, text='i found 1 face')
        else:
            bot.send_message(chat_id=update.message.chat_id, text=('i found ' + str(f) + ' faces'))
        bot.send_chat_action(chat_id=update.message.chat_id, action=tg.ChatAction.UPLOAD_PHOTO)
        time.sleep(1)
        bot.send_photo(chat_id=update.message.chat_id,
                       photo=open((filename[:(len(filename) - 4)] + '_result.png'), 'rb'))

    print("photo send by {} processed".format(update.message.chat.username))


def echo(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=tg.ChatAction.TYPING)
    time.sleep(2)
    print("unknown text send by ", update.message.chat.username, ": ", update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text="I can't inderstand you.\nconsider using  /info")


bot_dispatcher.add_handler(tgext.CommandHandler('start', start))
bot_dispatcher.add_handler(tgext.CommandHandler('help', bot_help))
bot_dispatcher.add_handler(tgext.CommandHandler('info', info))
bot_dispatcher.add_handler(tgext.MessageHandler(tgext.Filters.photo, picture))
bot_dispatcher.add_handler(tgext.MessageHandler('', echo))

bot_updater.start_polling()
bot_updater.idle()
