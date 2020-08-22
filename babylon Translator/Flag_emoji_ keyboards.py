try:
    import FlagTs
    from zipfile import ZipFile
    import time
    import telepot
    from telepot.loop import MessageLoop
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

except Exception as error:
    print('some thing went wrong'.format(error))


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    command = msg['text'].lower()
    user_message = msg['text'].lower()
    if user_message =='/start':   
    p = FlagTs(user_message)
    bot.sendMessage(chat_id,f'{user_message}')
    if command == '/start':
        markup = ReplyKeyboardMarkup(keyboard=[['🇿🇦', KeyboardButton(text='🇦🇱'), KeyboardButton(text='🇽🇰'), KeyboardButton(text='🇲🇪'), KeyboardButton(text='🇪🇷')], [
            dict(text='🇪🇹'), KeyboardButton(text='🇩🇿'), KeyboardButton(text='🇧🇭'), KeyboardButton(text='🇹🇩'), KeyboardButton(text='🇰🇲')], [
                                     dict(text='🇩🇯'), KeyboardButton(text='🇪🇬'), KeyboardButton(text='🇮🇶'), KeyboardButton(text='🇯🇴'), KeyboardButton(text='🇰🇼')], [
                                         dict(text='🇱🇧'), KeyboardButton(text='🇱🇾'), KeyboardButton(text='🇲🇷'), KeyboardButton(text='🇲🇦'), KeyboardButton(text='🇴🇲')], [
                                         dict(text='🇵🇸'), KeyboardButton(text='🇶🇦'), KeyboardButton(text='🇸🇦'), KeyboardButton(text='🇸🇴'), KeyboardButton(text='🇸🇩')], [
                                             dict(text='🇸🇾'), KeyboardButton(text='🇹🇳'), KeyboardButton(text='🇦🇪'), KeyboardButton(text='🇾🇪'), KeyboardButton(text='🇦🇲')], [
                                             dict(text='🇦🇿'), KeyboardButton(text='🇧🇩'), KeyboardButton(text='🇧🇦'), KeyboardButton(text='🇧🇬'), KeyboardButton(text='🇦🇩')], [
                                                 dict(text='🇲🇼'), KeyboardButton(text='🇨🇳'), KeyboardButton(text='🇹🇼'), KeyboardButton(text='🇭🇷'), KeyboardButton(text='🇧🇪')], [
                                                     dict(text='🇩🇰'), KeyboardButton(text='🇳🇱'), KeyboardButton(text='🇸🇷'), KeyboardButton(text='🇦🇬'), KeyboardButton(text='🇦🇺')], [
                                                         dict(text='🇧🇸'), KeyboardButton(text='🇧🇧'), KeyboardButton(text='🇧🇿'), KeyboardButton(text='🇧🇼'), KeyboardButton(text='🇨🇲')], [
                                                             dict(text='🇨🇦'), KeyboardButton(text='🇩🇲'), KeyboardButton(text='🇸🇿'), KeyboardButton(text='🇬🇲'), KeyboardButton(text='🇬🇭')], [
                                                                 dict(text='🇬🇩'), KeyboardButton(text='🇬🇾'), KeyboardButton(text='🇭🇰'), KeyboardButton(text='🇯🇲'), KeyboardButton(text='🇰🇪')],[
                                                                     dict(text='🇰🇮'), KeyboardButton(text='🇱🇸'), KeyboardButton(text='🇱🇷'), KeyboardButton(text='🇲🇭'), KeyboardButton(text='🇳🇦')],[
                                                                         dict(text='🇳🇷'), KeyboardButton(text='🇳🇬'), KeyboardButton(text='🇵🇼'), KeyboardButton(text='🇵🇬'), KeyboardButton(text='🇰🇳')],[
                                                                             dict(text='🇱🇨'), KeyboardButton(text='🇻🇨'), KeyboardButton(text='🇼🇸'), KeyboardButton(text='🇸🇨'), KeyboardButton(text='🇸🇱')],[
                                                                                 dict(text='🇸🇧'), KeyboardButton(text='🇸🇸'), KeyboardButton(text='🇹🇿'), KeyboardButton(text='🇹🇴'), KeyboardButton(text='🇹🇹')],[
                                                                                     dict(text='🇹🇻'), KeyboardButton(text='🇺🇬'), KeyboardButton(text='🇬🇧'), KeyboardButton(text='🇺🇸'), KeyboardButton(text='🇻🇺')],[
                                                                                         dict(text='🇿🇲'), KeyboardButton(text='🇿🇼'), KeyboardButton(text='🇪🇪'), KeyboardButton(text='🇵🇭'), KeyboardButton(text='🇫🇮')],[
                                                                                             dict(text='🇧🇯'), KeyboardButton(text='🇧🇫'), KeyboardButton(text='🇧🇮'), KeyboardButton(text='🇨🇫'), KeyboardButton(text='🇨🇩')],[
                                                                                                 dict(text='🇬🇶'), KeyboardButton(text='🇫🇷'), KeyboardButton(text='🇬🇦'), KeyboardButton(text='🇬🇳'), KeyboardButton(text='🇲🇱')],[
                                                                                                     dict(text='🇲🇨'), KeyboardButton(text='🇳🇪'), KeyboardButton(text='🇸🇳'), KeyboardButton(text='🇨🇭'), KeyboardButton(text='🇹🇬')],[
                                                                                                         dict(text='🇬🇪'), KeyboardButton(text='🇦🇹'), KeyboardButton(text='🇩🇪'), KeyboardButton(text='🇱🇮'), KeyboardButton(text='🇨🇾')],[
                                                                                                             dict(text='🇬🇷'), KeyboardButton(text='🇭🇹'), KeyboardButton(text='🇮🇱'), KeyboardButton(text='🇮🇳'), KeyboardButton(text='🇭🇺')],[
                                                                                                                 dict(text='🇮🇸'), KeyboardButton(text='🇮🇩'), KeyboardButton(text='🇮🇪'), KeyboardButton(text='🇮🇹'), KeyboardButton(text='🇸🇲')],[
                                                                                                                     dict(text='🇻🇦'), KeyboardButton(text='🇯🇵'), KeyboardButton(text='🇰🇿'), KeyboardButton(text='🇰🇵'), KeyboardButton(text='🇰🇷')],[
                                                                                                                         dict(text='🇽🇰'), KeyboardButton(text='🇱🇦'), KeyboardButton(text='🇱🇻'), KeyboardButton(text='🇱🇹'), KeyboardButton(text='🇱🇺')],[
                                                                                                                             dict(text='🇲🇬'), KeyboardButton(text='🇧🇳'), KeyboardButton(text='🇲🇾'), KeyboardButton(text='🇲🇹'), KeyboardButton(text='🇳🇿')],[
                                                                                                                                 dict(text='🇲🇳'), KeyboardButton(text='🇳🇵'), KeyboardButton(text='🇳🇴'), KeyboardButton(text='🇦🇫'), KeyboardButton(text='🇮🇷')],[
                                                                                                                                     dict(text='🇵🇱'), KeyboardButton(text='🇦🇴'), KeyboardButton(text='🇧🇷'), KeyboardButton(text='🇨🇻'), KeyboardButton(text='🇬🇼')],[
                                                                                                                                         dict(text='🇲🇴'), KeyboardButton(text='🇲🇿'), KeyboardButton(text='🇵🇹'), KeyboardButton(text='🇸🇹'), KeyboardButton(text='🇲🇩')],[
                                                                                                                                             dict(text='🇷🇴'), KeyboardButton(text='🇰🇬'), KeyboardButton(text='🇷🇺'), KeyboardButton(text='🇷🇸'), KeyboardButton(text='🇱🇰')],[
                                                                                                                                                 dict(text='🇨🇿'), KeyboardButton(text='🇸🇰'), KeyboardButton(text='🇸🇮'), KeyboardButton(text='🇦🇷'), KeyboardButton(text='🇨🇴')],[
                                                                                                                                                     dict(text='🇨🇷'), KeyboardButton(text='🇨🇺'), KeyboardButton(text='🇩🇴'), KeyboardButton(text='🇪🇨'), KeyboardButton(text='🇸🇻')],[
                                                                                                                                                         dict(text='🇬🇹'), KeyboardButton(text='🇭🇳'), KeyboardButton(text='🇲🇽'), KeyboardButton(text='🇳🇮'), KeyboardButton(text='🇵🇦')],[
                                                                                                                                                             dict(text='🇵🇾'), KeyboardButton(text='🇵🇪'), KeyboardButton(text='🇪🇸'), KeyboardButton(text='🇺🇾'), KeyboardButton(text='🇻🇪')],[
                                                                                                                                                                 dict(text='🇷🇼'), KeyboardButton(text='🇸🇪'), KeyboardButton(text='🇹🇯'), KeyboardButton(text='🇸🇬'), KeyboardButton(text='🇹🇭')],[
                                                                                                                                                                 dict(text='🇺🇦'), KeyboardButton(text='🇵🇰'), KeyboardButton(text='🇺🇿'), KeyboardButton(text='🇻🇳'),KeyboardButton(text='Back')], ], resize_keyboard=True)
        

        responce = bot.getChat(chat_id)
        first_name = responce['first_name']
        bot.sendMessage(chat_id, f'hello {first_name}', reply_markup=markup)


TOKEN = '1346878810:AAGj0p_Hoq1YZjm_K78YLTLc_7Q_NqkHbNo'
# your token
bot = telepot.Bot(TOKEN)
answerer = telepot.helper.Answerer(bot)

MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
