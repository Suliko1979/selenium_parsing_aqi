import selenium
import telebot
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

token = '1736982389:AAH8BhhcRC9JfTw1FCAJNQ9nnxtgqc89MWk'
bot = telebot.TeleBot(token)
welcome_text = "Привет! Качество воздуха в указанном городе сейчас: "

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text.lower() == 'привет' or "ghbdtn":
        bot.send_message(message.chat.id, "Для того, чтобы узнать уровень загрязнения воздуха в каком-либо городе, наберите название города")

@bot.message_handler(content_types=['text'])
def test(message):
    city_name = message.text
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.iqair.com/ru/mobile-search')
        time.sleep(5)
        find = driver.find_element_by_css_selector('.input > input:nth-child(1)')
        find.send_keys(city_name)
        time.sleep(7)
        driver.find_element_by_class_name('name').click()
        time.sleep(5)
        aqi = driver.find_element_by_css_selector('.aqi-status__text')
        time.sleep(3)
        aqi_num = driver.find_element_by_xpath('/html/body/app-root/app-portal-container/div/app-routes-resolver/div/app-city/div[2]/div[2]/app-aqi-overview/div/div[1]/div/div/p[2]')
        driver.close()
        bot.send_message(message.chat.id, welcome_text   +   aqi_num + " пунктов."
                          " \n Говоря словами, качество воздуха в категории  "
                         + aqi)
    except:
        bot.send_message(message.chat.id, "Город " + city_name + " не найден")

bot.polling()

