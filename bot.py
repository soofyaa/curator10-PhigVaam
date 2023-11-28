from telebot import TeleBot
from random import random # для подбора случайного числа
Mining = TeleBot('6637586538:AAEpFTn8wMw-1w1y-SWUiur0YCvK-HxF_tI') # называем бота

# следующий список содержит все возможные виды камня, которые могут быть написаны в dig()
stones = [['Камень 🔳', 'После удара киркой монолитный кусок рассыпается на кучу булыжников...', 'common', 0.93],
          ['Медь 🔶', 'Думаю, из него можно получить бронзу...', 'rare', 0.96],
          ['Останки ☠️', 'Отголоски Мезозойской эры 🐲', 'rare', 0.99],
          ['Золото 🏆', 'Не все то золото, что блестит...', 'epic', 0.997],
          ['Сокровища 💎', '💵 Ура! Теперь мы богаты! 💵', 'legendary', 1]]

# команда start()
@Mining.message_handler(commands=['start'])
def startDig(message):
    Mining.send_message(message.chat.id, "⛏ MINING SIMULATOR ALPHA: Напишите dig, чтобы начать копать! ⛏\n\n💰 Попробуйте найти сокровища! 💰")

# команда dig()
@Mining.message_handler(commands=['dig'])
def dig(message):
    chance = random() # рандомное число от 0 до 1 определяет, что именно будет выведено
    for i in stones: # проходимся по всему списку в поисках подходящего числа
        if chance <= i[-1]: # если рандомное число меньше определенного числа, прописанного в stones
            name, desc, rarity = i[0], i[1], i[2] # определяются надписи для выведения
            break # прервать цикл, если мы нашли число
    Mining.send_message(message.chat.id, ("Вы выкопали: " + name + '\n' + desc + '\nРедкость: ' + rarity))

Mining.infinity_polling()
