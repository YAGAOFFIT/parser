import logging
from aiogram.utils import executor
from create_bot import dp
# from handlers import add_profileFSM, control_profileFSM, main, regFSM, parser_controlFSM

async def on_startup(_):
    print('Бот в онлайне')

logging.basicConfig(level=logging.INFO)

# parser_controlFSM.reg_handlers_pars_fsm(dp)
# control_profileFSM.reg_handlers_edit_fsm(dp)
# add_profileFSM.reg_handlers_add_fsm(dp)
# regFSM.reg_handlers_reg_fsm(dp)
# main.reg_handlers_main(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup = on_startup)