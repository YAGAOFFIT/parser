from aiogram import Dispatcher, types
from create_bot import bot, db_clients
import markups.markups as nav

# проверка регистрации при первом сообщении
async def start_bot(message:types.Message):
    print(db_clients.user_exists(message.from_user.id))
    if (db_clients.user_exists(message.from_user.id) == False):
        db_clients.add_user(message.from_user.id)
        
    await bot.send_message(message.from_user.id, f'Приветствую, {message.from_user.first_name}\nТвой баланс', reply_markup=nav.chooseMainMenu)

# команда help которая не даст потеряться
async def helper(message:types.Message):
    await bot.send_message(message.from_user.id, f'Я типа еще не придумал что можно тут вписать {db_clients.get_balance()}')

# если вдруг бот потерялся и не понимает команды пользователя
async def dont_know(message:types.Message):
    await bot.send_message(message.from_user.id, 'Я не знаю такой команды, отправь /help и я помогу тебе!')

    
def reg_handlers_main(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_message_handler(helper, commands=['help'])
    dp.register_message_handler(dont_know)