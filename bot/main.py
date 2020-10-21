import constants
import functions

from fastai import *
from fastai.vision import *

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

bott = None
updater = Updater(constants.token, use_context=True)

bot = updater.bot

PATH   = "../models/tmp"
MODEL  = "stage-1_2.pkl"
learn = load_learner(os.path.abspath(PATH), MODEL) # обученная модель


def predict_single(img_file, learn):
    'function to take image and return prediction'
    classes = learn.data.classes
    prediction = learn.predict(open_image(img_file))
    probs_list = prediction[2].numpy()
    return {
        'category': classes[prediction[1].item()],
        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
    }


def start(update, context):
    pass




def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery

    query.answer()

    query.edit_message_text(text="Selected option: {}".format(query.data))


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    l_str = f'Update "{str(update)}" caused error "{str(context.error)}"', update, context.error
    functions.log_str_f(l_str)
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def mess_handler(update, context):
    functions.log_f(update.message, "-")
    print(update.message.text)
    print(update.message)
    print(update.message['photo'])
    print("================")
    print(update)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    #bot.send_message(1068755021, "Иди нахуй")


    #updater.dispatcher.add_handler(CommandHandler('start', answers.hello))
    #updater.dispatcher.add_handler(CallbackQueryHandler(answers.button))
    #updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)
    updater.dispatcher.add_handler(MessageHandler(Filters.text,mess_handler))
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
