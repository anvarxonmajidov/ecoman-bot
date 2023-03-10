from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


phone_btn=KeyboardButton(text='Telefon raqam',request_contact=True)

phone = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
phone.add(phone_btn)

viloyatlar=[
        'Toshkent shahri',
        'Toshkent viloyati',
        'Andijon viloyati',
        'Buxoro viloyati',
        'Farg\'ona viloyati',
        'Jizzax viloyati',
        'Xorazm viloyati',
        'Namangan viloyati',
        'Navoiy viloyati',
        'Qashqadaryo viloyati',
        'Qoraqalpog\'iston Respublikasi',
        'Samarqand viloyati',
        'Sirdaryo viloyati',
        'Surxondaryo viloyati'
        ]
location = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
for viloyat in viloyatlar:
    location.add(KeyboardButton(viloyat))



add_post = KeyboardButton('â Post qo\'shish')
balans = KeyboardButton('đ˛ Balans')
man_post = KeyboardButton('đ Postlar')
man_site = KeyboardButton('âšī¸ Biz haqimizda')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(add_post)
main_menu.add(balans)
main_menu.add(man_post)
main_menu.add(man_site)