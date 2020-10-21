import constants
from random import randint
import time


def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. ( id = {2} )\nТекст - {3}"
          .format(message.from_user.first_name,
                  message.from_user.last_name,
                  str(message.from_user.id),
                  message.text))
    print("Ответ - " + answer)


def log_f(message, answer):
    log_file = open(constants.log_file, 'a')
    from datetime import datetime
    l_str = ("[" + str(datetime.now())
             + "] Сообщение от {0} {1}. ( id = {2} ) Текст - {3}"
             .format(message.from_user.first_name,
                     message.from_user.last_name,
                     str(message.from_user.id),
                     message.text)
             + " Ответ - "
             + answer
             + "\n")
    log_file.write(l_str)
    log_file.close()


def log_e_f(exception):
    log_file = open(constants.log_file, 'a')
    from datetime import datetime
    l_str = f'[{str(datetime.now())}] EXCEPTION: {type(exception)} {str(exception)}\n'
    log_file.write(l_str)
    log_file.close()


def log_str_f(text):
    log_file = open(constants.log_file, 'a')
    from datetime import datetime
    l_str = f"[{str(datetime.now())}] {text}"
    log_file.write(l_str)
    log_file.close()


def is_admin(u_id):
    if u_id in constants.admins:
        return True
    else:
        return False


