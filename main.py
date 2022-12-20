import telebot
import random

from env import token 

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('yes')
button2 = telebot.types.KeyboardButton('no')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start','hi'])
def start_function(message):
    # print(message.chat.id)

    msg = bot.send_message(message.chat.id,f'привет{ message.chat.first_name} начнем игру',reply_markup=keyboard)
    bot.register_next_step_handler(msg,answer_check)
#     bot.send_sticker(message.chat.id, 
#     'CAACAgIAAxkBAAJKbWOhPeqQHfVr3EXcvph1blpGvDBSAAIFAQACMNSdEeO5qnacHgZLLAQ')
#     bot.send_photo(message.chat.id, 
#     'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cdc.gov%2Fhealthypets%2Fpets%2Fdogs.html&psig=AOvVaw3CrQ94JlIuEuuC9MNKROnp&ust=1671598378608000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJj1r7Kzh_wCFQAAAAAdAAAAABAF')
# bot.polling()
def answer_check(msg):
    if msg.text=='yes':
        bot.send_message(msg.chat.id,' у тебя есть 3 попытки угодать число от 1 до 10')
        random_numder=random.randint(1,10)
        p = 3
        start_game(msg, random_numder,p)

    else:
     bot.send_message(msg.chat.id,"ну и ладно")

def start_game(msg, random_numder,p):
    msg = bot.send_message(msg.chat.id, 'введите число от 1 до 10:') # 1, 2, 5
    bot.register_next_step_handler(msg,check_number, p-1, random_numder)


def check_number(msg, random_numder,p):# 5
    if msg.text == str(random_numder):
        bot.send_message(msg.chat.id,' вы победили')
    elif p == 0:
        bot.send_message(msg.chat.id,'вы проиграли , число было -{random_number}')
    else:
        bot.send_message(msg.chat.id, f'попробуй еще раз .тебя осталось {p} попыток')
        start_game(msg, p, random_numder,) # 2 , 3 ,1


# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id,message.text)

bot.polling()


# git init 
# git add 

# git commit -m 'names commit '
# git remotte add origin ssh/https 
# git push origin master



