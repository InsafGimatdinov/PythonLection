# from isOdd import isOdd

# print(isOdd(1)) 
# print(isOdd(4)) 

# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(2)
#     # Do some work
#     bar.next()
# bar.finish()

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 2, 3, 2, 7]

# plt.plot(list)

# plt.show()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5116717460:AAHIQ9MjZE9fgOIlF33Ge2enuTeJHh2H8kY')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

print('server start')
updater.start_polling()
updater.idle()