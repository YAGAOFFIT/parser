import logging
from aiogram.utils import executor
from create_bot import dp

# Импорт из папки нужных файлов
from handlers import main

async def on_startup(_):
    print('Бот в онлайне')

# Подключение базы данных
logging.basicConfig(level=logging.INFO)

# ! Запуск различных машин состояния
main.reg_handlers_main(dp)
# parser_controlFSM.reg_handlers_pars_fsm(dp)
# control_profileFSM.reg_handlers_edit_fsm(dp)
# add_profileFSM.reg_handlers_add_fsm(dp)
# regFSM.reg_handlers_reg_fsm(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup = on_startup)