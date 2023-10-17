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

# ! Переименовать в регистрацию и заполнить чат id и username
    def add_user(self, user_id): # регистрация нового клиента
        with self.connection:
            result = self.cursor.execute("INSERT INTO `users` (`id`) VALUES (?)", (user_id,))
            return result

    def user_exists(self, user_id): # Проверка нахождения клиента в базе
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def get_balance(self, user_id): # Проверка нахождения клиента в базе
        with self.connection:
            result = self.cursor.execute("SELECT `balance` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            print(result)
        
    def set_signup(self, user_id, signup): # Запись статуса клиента
        with self.connection:
            result = self.cursor.execute("UPDATE `users` SET `signup` = ?WHERE `user_id` = ?", (signup, user_id,))
            return result
