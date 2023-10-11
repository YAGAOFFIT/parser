import sqlite3

class Datebase:
    # ________________________________________________________
    # ________________________________________________________
    # ! Взаимодействие с таблицей users
    # ________________________________________________________
    # ________________________________________________________
    
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id): # регистрация нового клиента
        with self.connection:
            result = self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
            return result

    def user_exists(self, user_id): # Проверка нахождения клиента в базе
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_nickname(self, user_id, nickname): # Запись username клиента
        with self.connection:
            result = self.cursor.execute("UPDATE `users` SET `nick` = ? WHERE `user_id` = ?", (nickname, user_id,))
            return result

    def get_signup(self, user_id): # Полечение статуса регистрации клиента
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup
        
    def set_signup(self, user_id, signup): # Запись статуса клиента
        with self.connection:
            result = self.cursor.execute("UPDATE `users` SET `signup` = ?WHERE `user_id` = ?", (signup, user_id,))
            return result
    

    # ________________________________________________________
    # ________________________________________________________
    # Взаимодействие с таблицей profiles
    # ________________________________________________________
    # ________________________________________________________


    def add_new_req(self, name): # Создание нового профиля
        with self.connection:
            result = self.cursor.execute("INSERT INTO `profiles` (`name`) VALUES (?)", (name,))
        return result    

    def profile_exist(self, user_id): # Проверка нахождения профиля в базе
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `profiles` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_id(self, user_id, name): # Запись id клиента в базу с профилями
        with self.connection:
            result = self.cursor.execute("UPDATE `profiles` SET `user_id` = ? WHERE `name` = ?", (name, user_id,))
            return result

    def set_api_vk(self, name, vk_api): # Запись API профиля
        with self.connection:
            result = self.cursor.execute("UPDATE `profiles` SET `api` = ? WHERE `name` = ?", (vk_api, name,))
            return result


    def get_all_name_vk(self, user_id): # Получение всех имен профилей
        with self.connection:
            result = self.cursor.execute("SELECT `name` FROM `profiles` WHERE `user_id` = ?", (user_id,)).fetchall()
            name_list = []
            for el in result:
                name_list.append(el[0])
            return name_list

    def update_name(self, user_id, name, new_name): # Обновление имения профиля
        with self.connection:
            id = self.cursor.execute("SELECT `id` FROM `profiles` WHERE `user_id` = ? AND `name` = ?", (user_id, name,)).fetchall()
            id = id[0]
            id = id[0]
            result = self.cursor.execute("UPDATE `profiles` SET `name` = ? WHERE `id`= ?",(new_name, id,))
            return result

    def update_api(self, user_id, name, new_api): # Обновление API ключа
        with self.connection:
            return self.cursor.execute("UPDATE `profiles` SET `api` = ? WHERE `user_id` = ? AND `name`= ?",(new_api, user_id, name,))

    def get_api_vk(self, user_id, name): # Получение API профиля
        with self.connection:
            result = self.cursor.execute("SELECT `api` FROM `profiles` WHERE `user_id` = ? AND `name` = ?", (user_id, name,)).fetchall()
            el = result[0]
            return el[0]

    def delete_acc(self, name): # Удаление из списка аккаунта
        with self.connection:
            return self.cursor.execute("DELETE FROM `profiles` WHERE `name`= ?",(name,))

    def get_profile_status(self, user_id, name): # Получение статуса профиля 
        with self.connection:
            res = self.cursor.execute("SELECT `status` FROM `profiles` WHERE `name`= ? AND `user_id` = ?", (name, user_id,)).fetchall()
            res = res[0]
            res = res[0]
            return int(res)

    def set_profile_status(self, new_status, user_id, name): # Перезапись статуса аккаунта VK, 0 - это парсер не запущен, 1 - парсер работает, 2 - режим запуска
        with self.connection:
            return self.cursor.execute("UPDATE `profiles` SET `status`= ? WHERE `user_id` = ? AND `name` = ?",(new_status, user_id, name,))

    def set_profile_group(self, new_group, user_id, status): # Ввод ID группы
        with self.connection:
            return self.cursor.execute("UPDATE `profiles` SET `group_id`= ? WHERE `user_id` = ? AND `status` = ?",(new_group, user_id, status,))

    def get_profile_group(self, user_id, status):
        with self.connection:
            res = self.cursor.execute("SELECT `group_id` FROM `profiles` WHERE `user_id`= ? AND `status` = ?", (user_id, status,)).fetchall()
            res = res[0]
            res = res[0]
            return str(res)

    def get_profile_group_from_name(self, user_id, name):
        with self.connection:
            res = self.cursor.execute("SELECT `group_id` FROM `profiles` WHERE `user_id`= ? AND `name` = ?", (user_id, name,)).fetchall()
            res = res[0]
            res = res[0]
            return str(res)
    

    def get_api_vk_from_status(self, user_id, status): # Получение API профиля через статус редактирования
        with self.connection:
            result = self.cursor.execute("SELECT `api` FROM `profiles` WHERE `user_id` = ? AND `status` = ?", (user_id, status,)).fetchall()
            res = result[0]
            return res[0]

    def set_state_parser(self, state, user_id, name): # Запись количества добавленных людей
        with self.connection:
            return self.cursor.execute("UPDATE `profiles` SET `state_parser` = ? WHERE `name` = ? AND `user_id` = ?", (state, name, user_id))
    
    def get_state_parser(self, user_id, name): # Получение количества добавленных людей
        with self.connection:
            result = self.cursor.execute("SELECT `state_parser` FROM `profiles` WHERE `user_id` = ? AND `name` = ?", (user_id, name,)).fetchall()
            res = result[0]
            return res[0]
    
    def count_active_account_pars(self, status):
        with self.connection:
            result = self.cursor.execute("SELECT `name` FROM `profiles` WHERE `status` = ?", (status,)).fetchall()
            res = result[0]
            return len(res)

            

    

    




