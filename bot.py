from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import logging
import settings
import ephem

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

def get_planet(update, contex):
    try:
        user_text = update.message.text.split()
        planet_name = user_text[1].capitalize()
        planet = getattr(ephem, planet_name, None)

        if planet:
            position = ephem.constellation(planet(ephem.now()))
            update.message.reply_text(f"{planet_name} is currently in the constellation {position[1]}.")
        else:
            update.message.reply_text("Invalid planet name. Please provide a valid planet name.")
    except IndexError:
        update.message.reply_text("Please provide the name of the planet.")


def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Bot on')

    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()

main()