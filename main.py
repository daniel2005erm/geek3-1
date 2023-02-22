from aiogram import Bot,Dispatcher,types,executor
import config

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'go'])
async def start(message:types.Message):
    print(message)
    await message.answer(F'Здраствуйте {message.from_user.full_name}, {message.from_user.ur}')

@dp.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.reply("Вот мои комманды:")

@dp.message_handler(commands=['Привет'])
async def help(message:types.Message):
    await message.ahswer("Привет")

@dp.message_handler(commands=['about'])
async def about(message:types.Message):
    await message.answer(F"{message.from_user.as_json()}")
    await message.answer(F"Фамилия: {message.from_user.fist_name}\Имя: (message.from_user.last_name)\Username: {message.from_user.username}")
    await message.ansewer_photo("https://anime-fans.ru/wp-content/uploads/2022/04/CHyornyj-Klever-Glava-331-Data-Vyhoda-Asta-i-Ego-Neozhidannye-Sily.jpg")
    await message.ansewer_location(4, 1)
    with open('geeks.webp', 'rd') as g:
        await message.answer_photo(g.read())
    
@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /hepl")

executor.start_polling(dp)