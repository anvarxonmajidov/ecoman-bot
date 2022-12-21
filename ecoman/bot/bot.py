from aiogram import executor, types
from bot_header import API_TOKEN, dp,bot
from aiogram.dispatcher.filters import Text
import markup as kb
import sys,requests,json
sys.path.append('../')
from ecoman.settings import WEBSITE_URL
# conf
main={"add":0,"step":0}

# api

def get_posts(id):
    req=requests.get(f'{WEBSITE_URL}/get_posts/{id}/')
    return req.json()

def get_balans(id):
    req=requests.get(f'{WEBSITE_URL}/get_balans/{id}/')
    return req.json()['ecoin']

def get_step(id):
    req=requests.get(f'{WEBSITE_URL}/get_step/{id}/')
    return req.json()['qadam']

def increment_step(id):
    req=requests.get(f'{WEBSITE_URL}/increment_step/{id}/')
    return req.json()['qadam']

def get_add(id):
    req=requests.get(f'{WEBSITE_URL}/get_add/{id}/')
    return req.json()['qadam']

def increment_add(id):
    req=requests.get(f'{WEBSITE_URL}/increment_add/{id}/')
    return req.json()['qadam']

def decrement_add(id,url):
    data={
        'image':url
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    req=requests.post(f'{WEBSITE_URL}/decrement_add/{id}/',data=json.dumps(data), headers=headers)
    return req.json()['qadam']

@dp.message_handler(lambda msg:msg.text=='ℹ️ Biz haqimizda')
async def about(message: types.Message):
    await message.answer("Bu bot Ateam jamoasi tomonidan MohirFest Xakatoni uchun yaratildi!")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    data={
        'telegram_id':message.from_id
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    req=requests.post(f'{WEBSITE_URL}/create_user/',data=json.dumps(data), headers=headers)
    res_data=req.json()['qadam']
    if res_data==2:
        await message.reply(f'Hurmatli <b>{message.from_user.first_name}</b>.\nSiz muvaffaqiyatli ro\'yxatdan o\'tgansiz!!!',parse_mode='html',reply_markup=kb.main_menu)
    else:
        await message.reply("Telefon raqamingizni kiriting!",reply_markup=kb.phone)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_phone(message: types.Message):
    data={
        'phone':message.contact.phone_number,
        'ism':message.from_user.first_name,
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    req=requests.post(f'{WEBSITE_URL}/set_phone/{message.from_id}/',data=json.dumps(data), headers=headers)
    res_data=req.json()['qadam']
    await message.answer("Hududingizni tanlang!",reply_markup=kb.location)

@dp.message_handler(lambda msg:msg.text=='➕ Post qo\'shish')
async def add_post(message: types.Message):
    increment_add(message.from_id)
    await message.answer("Rasm jo'nating!")

@dp.message_handler(lambda msg:msg.text=='📝 Postlar')
async def get_post(message: types.Message):
    await message.answer("Sizning postlaringiz yuklanmoqda...")
    posts=get_posts(message.from_id)
    for post in posts:
        a="✅tasdiqlangan!"if post['tasdiq'] else "❎tasdiqlanmagan!"
        await bot.send_photo(message.chat.id,
        photo=types.InputFile.from_url(post['link']),
        caption=a
        )
    await message.answer("Sizning postlaringiz!")


@dp.message_handler(lambda msg:msg.text=='💲 Balans')
async def about(message: types.Message):
    await message.answer(f"Sizning balansingiz {get_balans(message.from_id)}🟢 Ecoin")

@dp.message_handler()
async def echo(message: types.Message):
    if get_step(message.from_id):
        viloyat=message.text
        data={
            'city':viloyat
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        req=requests.post(f'{WEBSITE_URL}/increment_step/{message.from_id}/',data=json.dumps(data), headers=headers)
        req.json()['qadam']
        await message.answer(f'Hurmatli <b>{message.from_user.first_name}</b>.\nSiz muvaffaqiyatli ro\'yxatdan o\'tdingiz!!!',parse_mode='html',reply_markup=kb.main_menu)
    else:
        await message.answer('Mavjud emas buyruq!')

@dp.message_handler(content_types=['photo','document'])
async def handle_docs_photo(message):
    # clear_folder('photos')
    if get_add(message.from_id,):
        if message.content_type == 'photo':
            file_photo = await bot.get_file(message.photo[-1].file_id)
            file_url=f'https://api.telegram.org/file/bot{API_TOKEN}/{file_photo.file_path}'
            decrement_add(message.from_id,file_url)
            await message.answer("Post yuborildi!")
        elif message.content_type == 'document':
            file_photo = await bot.get_file(message.document.file_id)
            if file_photo.file_path.endswith((".jpg",".png")):
                file_url=f'https://api.telegram.org/file/bot{API_TOKEN}/{file_photo.file_path}'
                decrement_add(message.from_id,file_url)
                await message.answer("Post yuborildi!")
            else:
                await message.answer("Iltimos faqat PNG yoki JPEG file jo'nating!")
    else:
        await message.answer("\"➕ Post qo\'shish\" tugmasidan foydalaning!")


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
