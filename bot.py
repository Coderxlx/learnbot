from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(update, context):
    text = "/start викликаний"
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = f"Привіт {update.message.chat.first_name}! Ти написав {update.message.text}."
    logging.info(f"User: {update.message.chat.username}, chat id: {update.message.chat.id} message: {update.message.text}")
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Bot on')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()

main()