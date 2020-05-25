# -*- coding: utf-8 -*-
import telebot
import pymysql

bot = telebot.TeleBot('1259983135:AAHTTe2W6wVbSOEqmj1x7gQaOtiSNAtBpNc')
print("sdfsd")

def averaage_org():
    con = pymysql.connect('us-cdbr-iron-east-01.cleardb.net', 'b03bd7c49246f6',
                          'b5c3d3de', 'heroku_b232c1733cdfc96')
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT avg(rating) FROM heroku_b232c1733cdfc96.interviews;")
        rating=cur.fetchone()
        element = str(rating[0])
        element = element[:3]
        stroka=str("Средний балл организации: {} ".format(element))
    return stroka

def averaage_otd():
    con = pymysql.connect('us-cdbr-iron-east-01.cleardb.net', 'b03bd7c49246f6',
                          'b5c3d3de', 'heroku_b232c1733cdfc96')
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT name,avg(rating) FROM heroku_b232c1733cdfc96.interviews group by name;")
        rating=cur.fetchall()
        stroka="Средний балл по отделениям:\n"
        for row in rating:
            element=str(row[1])
            element=element[:3]
            stroka+="{0}: {1}".format(row[0], element)+"\n"
    return stroka

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Средний балл по организации', 'Средний балл по отделениям')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую Вас, в Telegram Bote для просмотра результатов соц. опроса в организации РНПЦ ОМР',reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'средний балл по организации':
        bot.send_message(message.chat.id, averaage_org(),reply_markup=keyboard1)
    elif message.text.lower() == 'средний балл по отделениям':
        bot.send_message(message.chat.id, averaage_otd(),reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, 'Я не знаю такой команды',reply_markup=keyboard1)


bot.polling()
