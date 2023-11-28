from telebot import TeleBot
from random import random # для подбора случайного числа
Mining = TeleBot('6940480354:AAHYUUl-Tg64KVgkgTO5zjsMgT_KLHXT6PQ') # называем бота

stones = [
    ['Камень 🔳', 'После удара киркой монолитный кусок рассыпается на кучу булыжников...', 'common', 0.93],
    ['Медь 🔶', 'Думаю, из него можно получить бронзу...', 'rare', 0.96],
    ['Останки ☠️', 'Отголоски Мезозойской эры 🐲', 'rare', 0.99],
    ['Золото 🏆', 'Не все то золото, что блестит...', 'epic', 0.997],
    ['Сокровища 💎', '💵 Ура! Теперь мы богаты! 💵', 'legendary', 1]
]

@Mining.message_handler(commands=['start'])
def startDig(message):
    Mining.send_message(message.chat.id, "⛏ MINING SIMULATOR ALPHA: Напишите dig, чтобы начать копать! ⛏\n\n💰 Попробуйте найти сокровища! 💰")

@Mining.message_handler(commands=['dig'])
def dig(message):
    chance = random()
    for i in stones:
        if chance <= i[-1]:
            name, desc, rarity, _ = i
            break
    Mining.send_message(message.chat.id, f"Вы выкопали: {name}\n{desc}\nРедкость: {rarity}")

Mining.polling(none_stop=True, interval=0)
