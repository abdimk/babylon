import sys
import time
import telepot
from gtts import gTTS
from googletrans import Translator
from googletrans import LANGUAGES
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
# start of online server proxy config

import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    if command == '/start':
        markup2 = ForceReply()
        # keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=''),next key]],resize_keyboard=True)
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='How does it work', url='https://telegra.ph/Lists-of-Languages-available-in-the-bot-08-12')]])
        responce = bot.getChat(chat_id)
        first_name = responce['first_name']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(
            chat_id, f'Hello <b>{first_name} </b>', parse_mode='html', reply_markup=markup2)
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, 'Welcome to <b>babylon<b> translator chat bot this bot will help you to translate different languges and helps you to explore more and to communicate better.',
                        parse_mode='html', reply_markup=markup)
    elif msg['text'] != '/start':
        message = msg['text'].lower()
        value = message.split(' ')
        if not '|' in value:
            markup = ReplyKeyboardRemove()
            translator = Translator()
            translation = translator.translate(f'{message}')
            translation_src_name = LANGUAGES[translation.src]
            bot.sendChatAction(chat_id, 'typing')
            bot.sendMessage(
                chat_id, f'Language has been detected <b>{translation_src_name}</b>', parse_mode='html', reply_markup=markup)
            bot.sendChatAction(chat_id, 'typing')
            time.sleep(0.5)
            bot.sendMessage(chat_id, f'{translation.text}', parse_mode='html')
            bot.sendChatAction(chat_id, 'UPLOAD_AUDIO')
            tts = gTTS(message, lang='en')
            tts.save('mk.mp3')
            with open('mk.mp3', 'rb') as speech:
                bot.sendChatAction(chat_id, 'UPLOAD_AUDIO')
                bot.sendVoice(chat_id, voice=speech, caption=None)
                speech.close()
        else:
            try:
                markup = ReplyKeyboardRemove()
                message = msg['text'].lower()
                value = message.split('|')
                user_text = value[0]
                user_dest = value[-1].strip()
                translator = Translator()
                translations = translator.translate(
                    f'{user_text}', dest=f'{user_dest}')
                user_dest_name = LANGUAGES[user_dest]
                user_src_name = LANGUAGES[translations.src]
                bot.sendChatAction(chat_id, 'typing')
                bot.sendMessage(
                    chat_id, f'From <b>{user_src_name}</b> to <b>{user_dest_name}</b>', parse_mode='html')
                bot.sendMessage(
                    chat_id, f'<b>{translations.text}</b>', parse_mode='html')
            except ValueError:
                bot.sendMessage(
                    chat_id, f'invalid destination! what does {user_dest} means see How does it works section!')


# get token from command-line
TOKEN = '1239352593:AAHOZkDwqlkgeyWAb6kjOPxlphQgWKGaJsw'

bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
